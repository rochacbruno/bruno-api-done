from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session
from ..db import engine, get_session
from ..models.user import User, UserIn, UserPatch, UserOut, UserOutList
from ..security import IsAuthenticated, IsAdmin

router = APIRouter()


def check(request: Request):
    print(f"log {request.headers}")
    return False


@router.get("/", response_model=UserOutList, dependencies=[Depends(check)])
async def list_users(session = Depends(get_session)):
    return session.query(User).all()


@router.get("/{username}", response_model=UserOut)
async def get_user(username, session = Depends(get_session)):
    user = session.query(User).where(
        User.username == username
    ).first()
    if not user:
        raise HTTPException(status_code=404)
    return user


@router.patch("/{username}", response_model=UserOut)
async def update_user(username, patch: UserPatch):
    with Session(engine) as session:
        user = session.query(User).where(
            User.username == username
        ).first()
        if not user:
            raise HTTPException(status_code=404)

        patch_data = patch.dict(
            exclude_unset=True, 
            exclude={"confirm_password"}
        )
        for key, value in patch_data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@router.post("/", response_model=UserOut, dependencies=[IsAdmin])
def create_user(user_data: UserIn):
    with Session(engine) as session:
        user = User(**user_data.dict())
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists")
        session.refresh(user)
        return user


@router.delete("/{username}")
def delete_user(username):
    with Session(engine) as session:
        user = session.query(User).where(
            User.username == username
        ).first()
        if not user:
            raise HTTPException(status_code=404)
        session.delete(user)
        session.commit()
        return {"ok": True}

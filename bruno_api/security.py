from pydantic import BaseModel
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


# dependencia
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
IsAuthenticated = Depends(oauth2_scheme)


async def is_admin(token: str = Depends(oauth2_scheme)):
    if token != "Bazinga":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

IsAdmin = Depends(is_admin)


class Token(BaseModel):
    access_token: str
    token_type: str


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    # Emite token
    if form_data.username == "admin" and form_data.password == "admin":
        return {
            "access_token": "Bazinga", "token_type": "bearer"
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

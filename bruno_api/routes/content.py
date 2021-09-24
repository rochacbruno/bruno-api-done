from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def list_contents():
    return []


@router.get("/{contentname}")
async def get_content(contentname):
    return contentname


@router.delete("/{content_id}")
async def delete_content(content_id: int):
    return {"ok": "Content deleted"}
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from .user import router as user_router
from .content import router as content_router

main_router = APIRouter()
main_router.include_router(user_router, prefix="/user", tags=["user"])
main_router.include_router(content_router, prefix="/content", tags=["content"])

@main_router.get("/")
async def index():
    return RedirectResponse("/redoc")
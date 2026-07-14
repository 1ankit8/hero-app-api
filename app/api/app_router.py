from fastapi import APIRouter
from app.api.routes.role import router as role_router
from app.api.routes.user import router as user_router

router = APIRouter(prefix="/api")

router.include_router(
    prefix="/users",
    tags=["users"],
    router=user_router
)

router.include_router(
    prefix="/roles",
    tags=["roles"],
    router=role_router
)

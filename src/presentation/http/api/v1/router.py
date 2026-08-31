from fastapi import APIRouter

from src.presentation.http.api.v1.routers.router import router as users_router


router = APIRouter(prefix="/v1")
router.include_router(users_router, prefix="/users")

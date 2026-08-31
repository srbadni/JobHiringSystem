from fastapi import APIRouter, status

from .schemas import UserCreate, UserRead

router = APIRouter(tags=["Users"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def create_user(user_data: UserCreate):
    pass

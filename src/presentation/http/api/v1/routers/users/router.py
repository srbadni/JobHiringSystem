from fastapi import APIRouter, status

from application.users.command.create_user import CreateUserCommand
from .schemas import UserCreate, UserRead

router = APIRouter(tags=["Users"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(user_data: UserCreate):
    command = CreateUserCommand(
        full_name=user_data.full_name,
        phone_number=user_data.phone_number,
        email=user_data.email,
        password=user_data.password,
        profile_image_url=user_data.profile_image_url,
        user_type=user_data.user_type
    )

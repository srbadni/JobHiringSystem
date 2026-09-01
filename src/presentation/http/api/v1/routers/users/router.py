from typing import Annotated

from fastapi import APIRouter, status, Depends

from application.users.command.create_user import CreateUserCommand
from application.users.handlers.create_user_handler import CreateUserCommandHandler
from .dependencies import get_create_user_command_handler
from .schemas import UserCreate, UserRead

router = APIRouter(tags=["Users"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(user_data: UserCreate, command_handler: Annotated[CreateUserCommandHandler, Depends(get_create_user_command_handler)]):
    command = CreateUserCommand(
        full_name=user_data.full_name,
        phone_number=user_data.phone_number,
        email=user_data.email,
        password=user_data.password,
        profile_image_url=user_data.profile_image_url,
        user_type=user_data.user_type
    )

    return await command_handler.handle(command)

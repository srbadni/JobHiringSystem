from collections.abc import Callable
from typing import Annotated

from fastapi import APIRouter, Depends, status

from application.users.command.create_user import CreateUserCommand
from application.users.handlers import GetUserByEmailQueryHandler, GetUserByIdQueryHandler, ListUsersQueryHandler, \
    CreateUserCommandHandler
from application.users.query.get_user_by_email import GetUserByEmailQuery
from application.users.query.get_user_by_id import GetUserByIdQuery
from application.users.query.list_users import ListUsersQuery

from .schemas import UserCreate, UserRead

CreateUserHandlerProvider = Callable[[], CreateUserCommandHandler]
GetUserByEmailHandlerProvider = Callable[[], GetUserByEmailQueryHandler]
GetUserByIdHandlerProvider = Callable[[], GetUserByIdQueryHandler]
ListUsersHandlerProvider = Callable[[], ListUsersQueryHandler]


def create_users_router(
        provide_create_user_handler: CreateUserHandlerProvider,
        provide_get_all_users_handler: ListUsersHandlerProvider,
        provide_get_user_by_id_handler: GetUserByIdHandlerProvider,
        provide_get_user_by_email_handler: GetUserByEmailHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Users"])

    @router.post(
        "",
        status_code=status.HTTP_201_CREATED,
        response_model=UserRead,
    )
    async def create_user( # pyright: ignore[reportUnusedFunction]
            user_data: UserCreate,
            command_handler: Annotated[
                CreateUserCommandHandler,
                Depends(provide_create_user_handler),
            ],
    ):
        command = CreateUserCommand(
            full_name=user_data.full_name,
            phone_number=user_data.phone_number,
            email=user_data.email,
            password=user_data.password,
            profile_image_url=user_data.profile_image_url,
            user_type=user_data.user_type,
        )

        return await command_handler.handle(command)

    @router.get("", response_model=list[UserRead])
    async def get_all_users( # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[ListUsersQueryHandler, Depends(provide_get_all_users_handler)]
    ):
        query = ListUsersQuery()

        return await query_handler.handle(query)

    @router.get("/{user_id}", response_model=UserRead)
    async def get_user_by_id(  # pyright: ignore[reportUnusedFunction]
            user_id: str,
            query_handler: Annotated[GetUserByIdQueryHandler, Depends(provide_get_user_by_id_handler)]
    ):
        query = GetUserByIdQuery(user_id=user_id)

        return await query_handler.handle(query)

    @router.get("/email/{email}", response_model=UserRead)
    async def get_user_by_email(  # pyright: ignore[reportUnusedFunction]
            email: str,
            query_handler: Annotated[GetUserByEmailQueryHandler, Depends(provide_get_user_by_email_handler)]
    ):
        query = GetUserByEmailQuery(email=email)

        return await query_handler.handle(query)

    return router
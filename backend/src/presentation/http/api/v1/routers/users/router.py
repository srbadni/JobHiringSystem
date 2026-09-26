from collections.abc import Callable
from typing import Annotated

from fastapi import APIRouter, Depends, status
from uuid import UUID
from domain.user.enums import UserType
from application.users.command.update_user import UpdateUserCommand
from application.users.command.delete_user import DeleteUserCommand
from application.users.handlers import UpdateUserCommandHandler, DeleteUserCommandHandler
from application.employer_registration.handlers.create_employer_handler import CreateEmployerHandler
from application.employer_registration.command.create_employer_and_company import CreateEmployerAndCompany
from application.companies.command.create_company import CreateCompanyCommand

from application.users.command.create_user import CreateUserCommand
from application.users.handlers import GetUserByEmailQueryHandler, GetUserByIdQueryHandler, ListUsersQueryHandler, \
    CreateUserCommandHandler
from application.users.query.get_user_by_email import GetUserByEmailQuery
from application.users.query.get_user_by_id import GetUserByIdQuery
from application.users.query.list_users import ListUsersQuery

from .schemas import UserCreate, UserRead, UserUpdate

CreateUserHandlerProvider = Callable[[], CreateUserCommandHandler]
GetUserByEmailHandlerProvider = Callable[[], GetUserByEmailQueryHandler]
GetUserByIdHandlerProvider = Callable[[], GetUserByIdQueryHandler]
ListUsersHandlerProvider = Callable[[], ListUsersQueryHandler]
UpdateUserHandlerProvider = Callable[[], UpdateUserCommandHandler]
DeleteUserHandlerProvider = Callable[[], DeleteUserCommandHandler]
CreateEmployerHandlerProvider = Callable[[], CreateEmployerHandler]


def create_users_router(
        provide_create_user_handler: CreateUserHandlerProvider,
        provide_get_all_users_handler: ListUsersHandlerProvider,
        provide_get_user_by_id_handler: GetUserByIdHandlerProvider,
        provide_get_user_by_email_handler: GetUserByEmailHandlerProvider,
        provide_update_user_handler: UpdateUserHandlerProvider,
        provide_delete_user_handler: DeleteUserHandlerProvider,
        provide_create_employer_handler: CreateEmployerHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Admin - Users"])

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
            user_type=UserType.APPLICANT,
        )

        return await command_handler.handle(command)

    @router.get("", response_model=list[UserRead])
    async def get_all_users( # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[ListUsersQueryHandler, Depends(provide_get_all_users_handler)],
            user_type: UserType | None = None,
    ):
        query = ListUsersQuery(user_type=user_type)

        return await query_handler.handle(query)

    @router.get("/{user_id}", response_model=UserRead)
    async def get_user_by_id(  # pyright: ignore[reportUnusedFunction]
            user_id: UUID,
            query_handler: Annotated[GetUserByIdQueryHandler, Depends(provide_get_user_by_id_handler)]
    ):
        query = GetUserByIdQuery(user_id=user_id)

        return await query_handler.handle(query)

    @router.get("/by-email/{email}", response_model=UserRead)
    async def get_user_by_email(  # pyright: ignore[reportUnusedFunction]
            email: str,
            query_handler: Annotated[GetUserByEmailQueryHandler, Depends(provide_get_user_by_email_handler)]
    ):
        query = GetUserByEmailQuery(email=email)

        return await query_handler.handle(query)

    @router.put("/{user_id}", response_model=UserRead)
    async def update_user(  # pyright: ignore[reportUnusedFunction]
            user_id: UUID, user_data: UserUpdate,
            command_handler: Annotated[UpdateUserCommandHandler, Depends(provide_update_user_handler)],
    ):
        return await command_handler.handle(UpdateUserCommand(user_id=user_id, **user_data.model_dump()))

    @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_user(  # pyright: ignore[reportUnusedFunction]
            user_id: UUID,
            command_handler: Annotated[DeleteUserCommandHandler, Depends(provide_delete_user_handler)],
    ) -> None:
        await command_handler.handle(DeleteUserCommand(user_id=user_id))

    return router

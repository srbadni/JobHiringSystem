from application.users.handlers import (
    CreateUserCommandHandler,
    GetUserByEmailQueryHandler,
    GetUserByIdQueryHandler,
    ListUsersQueryHandler,
)
from bootstrap.common_providers import password_hasher, provide_uow


def provide_create_user_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(
        uow=provide_uow(),
        hasher=password_hasher,
    )


def provide_get_all_users_handler() -> ListUsersQueryHandler:
    return ListUsersQueryHandler(
        uow=provide_uow(),
    )


def provide_get_user_by_id_handler() -> GetUserByIdQueryHandler:
    return GetUserByIdQueryHandler(
        uow=provide_uow(),
    )


def provide_get_user_by_email_handler() -> GetUserByEmailQueryHandler:
    return GetUserByEmailQueryHandler(
        uow=provide_uow(),
    )

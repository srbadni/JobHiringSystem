from application.authentication.handler.get_current_user_handler import GetCurrentUserHandler
from application.authentication.handler.login_handler import LoginHandler
from application.users.handlers import (
    CreateUserCommandHandler,
    GetUserByEmailQueryHandler,
    GetUserByIdQueryHandler,
    ListUsersQueryHandler,
    UpdateUserCommandHandler,
    DeleteUserCommandHandler,
)
from bootstrap.common_providers import password_hasher, provide_uow, provide_auth


def provide_login_handler() -> LoginHandler:
    return LoginHandler(
        uow=provide_uow(),
        hasher=password_hasher,
        auth=provide_auth(),
    )

def provide_get_current_user_handler() -> GetCurrentUserHandler:
    return GetCurrentUserHandler(
        uow=provide_uow(),
        auth=provide_auth(),
    )

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


def provide_update_user_handler() -> UpdateUserCommandHandler:
    return UpdateUserCommandHandler(uow=provide_uow())


def provide_delete_user_handler() -> DeleteUserCommandHandler:
    return DeleteUserCommandHandler(uow=provide_uow())

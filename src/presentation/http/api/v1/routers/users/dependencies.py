from typing import Annotated

from fastapi import Depends

from application.common.ports.unit_of_work import UnitOfWork
from application.users.handlers.create_user_handler import CreateUserCommandHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow
from infrastructure.security.pwdlib_password_hasher import PwdlibPasswordHasher


def get_create_user_command_handler(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> CreateUserCommandHandler:
    return CreateUserCommandHandler(uow=uow, hasher=PwdlibPasswordHasher())
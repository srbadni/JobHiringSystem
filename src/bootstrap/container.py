"""Application composition root.

Only this module knows both the application's abstractions and their concrete
infrastructure implementations.
"""

from application.users.handlers.create_user_handler import CreateUserCommandHandler
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal
from infrastructure.persistence.sqlalchemy.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.security.pwdlib_password_hasher import PwdlibPasswordHasher


def create_user_command_handler() -> CreateUserCommandHandler:
    """Build a create-user handler for one HTTP request."""
    return CreateUserCommandHandler(
        uow=SqlAlchemyUnitOfWork(AsyncSessionLocal),
        hasher=PwdlibPasswordHasher(),
    )

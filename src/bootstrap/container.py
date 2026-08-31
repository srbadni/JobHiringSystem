from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from application.users.handlers.create_user_handler import CreateUserCommandHandler
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal
from infrastructure.security.pwdlib_password_hasher import PwdlibPasswordHasher


class Container:
    """Application composition root for infrastructure-backed use cases."""

    def __init__(self) -> None:
        self._session_factory = AsyncSessionLocal
        self._password_hasher = PwdlibPasswordHasher()

    @asynccontextmanager
    async def create_user_handler(self) -> AsyncIterator[CreateUserCommandHandler]:
        # A handler and its repository share one request-scoped transaction.
        async with self._session_factory.begin() as session:
            repository = SqlAlchemyUserRepository(session)
            yield CreateUserCommandHandler(repository, self._password_hasher)

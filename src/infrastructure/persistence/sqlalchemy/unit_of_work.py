from typing import Any

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.common.ports.unit_of_work import UnitOfWork
from .repositories.sqlalchemy_user_repository import (
    SqlAlchemyUsersRepository,
)
from .session import AsyncSessionLocal


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession | Any]):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = SqlAlchemyUsersRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        try:
            await super().__aexit__(exc_type, exc_value, traceback)
        finally:
            await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


def get_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(AsyncSessionLocal)
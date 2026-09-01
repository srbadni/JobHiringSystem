from application.common.ports.unit_of_work import UnitOfWork
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SqlAlchemyUsersRepository
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.users = SqlAlchemyUsersRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            super().__exit__(exc_type, exc_value, traceback)
        finally:
            self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


async def get_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(AsyncSessionLocal)
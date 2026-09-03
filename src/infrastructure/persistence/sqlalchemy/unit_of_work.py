from types import TracebackType
from typing import Any

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.common.ports.unit_of_work import UnitOfWork
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_company_repository import SQLAlchemyCompanyRepository
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_company_membership_repository import SqlAlchemyCompanyMembershipRepository
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_job_posting_repository import SqlAlchemyJobPostingRepository
from infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_jobs_search_repository import SQLAlchemyJobsSearchRepository
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
        self.companies = SQLAlchemyCompanyRepository(self.session)
        self.company_memberships = SqlAlchemyCompanyMembershipRepository(self.session)
        self.job_postings = SqlAlchemyJobPostingRepository(self.session)
        self.jobs_search = SQLAlchemyJobsSearchRepository(self.session)

        return self

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        try:
            await super().__aexit__(exc_type, exc_val, exc_tb)
        finally:
            await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


def get_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(AsyncSessionLocal)
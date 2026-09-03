from abc import ABC, abstractmethod

from application.jobs_search.ports.jobs_search_repository import JobsSearchRepository

from ...job_posting.ports.job_posting_respository import JobPostingRepository

from ...companies.ports.repositories.company_repository import CompanyRepository
from ...company_membership.ports.company_membership_repository import CompanyMembershipRepository

from ...users.ports.users_repository import UsersRepository

from types import TracebackType


class UnitOfWork(ABC):
    users: UsersRepository
    companies: CompanyRepository
    company_memberships: CompanyMembershipRepository
    job_postings: JobPostingRepository
    jobs_search: JobsSearchRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass
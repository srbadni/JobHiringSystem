from application.common.ports.unit_of_work import UnitOfWork
from domain.job_posting.models import JobPosting

from ..query.list_job_postings import ListJobPostingsQuery


class ListJobPostingsQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListJobPostingsQuery) -> list[JobPosting]:
        async with self.uow:
            return await self.uow.job_postings.list(query.company_id)

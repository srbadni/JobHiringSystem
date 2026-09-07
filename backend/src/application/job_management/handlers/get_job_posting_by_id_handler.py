from application.common.ports.unit_of_work import UnitOfWork
from domain.job_posting.models import JobPosting

from ..query.get_job_posting_by_id import GetJobPostingByIdQuery


class GetJobPostingByIdQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetJobPostingByIdQuery) -> JobPosting:
        async with self.uow:
            return await self.uow.job_postings.get_by_id(query.job_posting_id, query.company_id)

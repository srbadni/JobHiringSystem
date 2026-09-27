import uuid

from application.common.ports.unit_of_work import UnitOfWork
from domain.job_posting.models import JobPosting

from ..query.get_job_posting_by_id import GetJobPostingByIdQuery


class GetJobPostingByIdQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetJobPostingByIdQuery) -> JobPosting | None:
        async with self.uow:
            company_membership = await self.uow.company_memberships.get_by_user_id(uuid.UUID(query.user_id))
            if company_membership:
                return await self.uow.job_postings.get_by_id(query.job_posting_id, company_membership.company_id)
            return None

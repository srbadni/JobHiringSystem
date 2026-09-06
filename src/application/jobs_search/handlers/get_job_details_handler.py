from ..ports.jobs_search_repository import GetJobDetailsQueries
from ..query.get_job_details_query import GetJobDetailsQuery
from ...common.ports.unit_of_work import UnitOfWork


class GetJobDetailsHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetJobDetailsQuery):
        async with self.uow:
            return await self.uow.jobs_search.get_job_details(GetJobDetailsQueries(
                job_posting_id=query.job_posting_id,
                company_en_name=query.company_en_name,
            ))
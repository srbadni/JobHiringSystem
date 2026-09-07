from ..dto.job_search_result import JobSearchResult
from ..ports.jobs_search_repository import GetCompanyJobsQueries
from ..query.get_company_jobs import GetCompanyJobs
from ...common.ports.unit_of_work import UnitOfWork


class GetCompanyJobsHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetCompanyJobs) -> list[JobSearchResult]:
        async with self.uow:
            return await self.uow.jobs_search.get_company_jobs(GetCompanyJobsQueries(
                company_en_name=query.company_en_name,
            ))
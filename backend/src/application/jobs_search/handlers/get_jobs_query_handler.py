from application.common.ports.unit_of_work import UnitOfWork
from application.jobs_search.dto.job_search_result import JobResults
from application.jobs_search.ports.jobs_search_repository import GetJobsQueries
from application.jobs_search.query.get_jobs import GetJobsQuery


class GetJobsQueryHandler:
    def __init__(
        self,
        uow: UnitOfWork,
    ) -> None:
        self.uow = uow

    async def handle(self, query: GetJobsQuery) -> JobResults:
        async with self.uow:
            return await self.uow.jobs_search.get_jobs(GetJobsQueries(
                keywords=query.keywords,
                province_ids=query.province_ids,
                job_category_ids=query.job_category_ids,
                work_modes=query.work_modes,
                work_experiences=query.work_experiences,
                salary_range_ids=query.salary_range_ids,
                page_size=query.page_size,
                page_index=query.page_index,
                sort_type=query.sort_type,
            ))

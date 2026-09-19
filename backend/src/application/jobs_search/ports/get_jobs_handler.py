from typing import Protocol

from application.jobs_search.dto.job_search_result import JobResults
from application.jobs_search.query.get_jobs import GetJobsQuery


class GetJobsHandler(Protocol):
    async def handle(self, query: GetJobsQuery) -> JobResults:
        ...

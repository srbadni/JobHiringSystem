from uuid import UUID
from typing import Annotated, Callable

from fastapi import APIRouter, Depends, Query

from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from application.jobs_search.query.get_jobs import GetJobsQuery
from domain.job_posting.enum import RelevantWorkExperience, WorkMode

JobsResultHandlerProvider = Callable[[], GetJobsQueryHandler]

def create_jobs_result_router(
    provide_jobs_result_handler: JobsResultHandlerProvider
) -> APIRouter:
    router = APIRouter(tags=["Jobs Result"])

    @router.get("")
    async def get_jobs_result( # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[GetJobsQueryHandler, Depends(provide_jobs_result_handler)],
            keywords: str | None = None,
            province_ids: list[UUID] | None = Query(default=None),
            job_category_ids: list[UUID] | None = Query(default=None),
            work_modes: list[WorkMode] | None = Query(default=None),
            work_experiences: list[RelevantWorkExperience] | None = Query(default=None),
            salary_range_ids: list[UUID] | None = Query(default=None),
    ):
        queries = GetJobsQuery(
            keywords=keywords,
            province_ids=province_ids,
            job_category_ids=job_category_ids,
            work_modes=work_modes,
            work_experiences=work_experiences,
            salary_range_ids=salary_range_ids,
        )
        return await query_handler.handle(query=queries)

    return router
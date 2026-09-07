from collections.abc import Callable
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Query
from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from application.jobs_search.query.get_jobs import GetJobsQuery
from domain.job_posting.enum import RelevantWorkExperience, WorkMode
from .schemas import JobSearchRead

def create_jobs_router(provide_handler: Callable[[], GetJobsQueryHandler]) -> APIRouter:
    router = APIRouter(tags=["Applicant - Jobs"])
    @router.get("/search", response_model=list[JobSearchRead])
    async def search(  # pyright: ignore[reportUnusedFunction]
        handler: Annotated[GetJobsQueryHandler, Depends(provide_handler)], keywords: str | None = None,
        province_ids: list[UUID] | None = Query(default=None), job_category_ids: list[UUID] | None = Query(default=None),
        work_modes: list[WorkMode] | None = Query(default=None), work_experiences: list[RelevantWorkExperience] | None = Query(default=None),
        salary_range_ids: list[UUID] | None = Query(default=None)):
        return await handler.handle(GetJobsQuery(keywords=keywords, province_ids=province_ids, job_category_ids=job_category_ids,
            work_modes=work_modes, work_experiences=work_experiences, salary_range_ids=salary_range_ids))
    return router

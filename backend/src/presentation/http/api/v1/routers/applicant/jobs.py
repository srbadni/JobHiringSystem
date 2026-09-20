import json
from collections.abc import Callable
from types import SimpleNamespace
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Query

from application.common.heplers.serialization_handler import serialization_handler
from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from application.jobs_search.query.get_jobs import GetJobsQuery, SortType
from domain.job_posting.enum import RelevantWorkExperience, WorkMode
from redis_fastapi import CacheBackendDep


def create_jobs_router(provide_handler: Callable[[], GetJobsQueryHandler]) -> APIRouter:
    router = APIRouter(tags=["Applicant - Jobs"])

    @router.get("/search")
    async def search(  # pyright: ignore[reportUnusedFunction]
            cache: CacheBackendDep,
            handler: Annotated[GetJobsQueryHandler, Depends(provide_handler)],
            keywords: str | None = None,
            province_ids: list[UUID] | None = Query(default=None),
            job_category_ids: list[UUID] | None = Query(default=None),
            work_modes: list[WorkMode] | None = Query(default=None),
            work_experiences: list[RelevantWorkExperience] | None = Query(default=None),
            salary_range_ids: list[UUID] | None = Query(default=None),
            page_size: int = Query(),
            page_index: int = Query(),
            sort_type: SortType | None = Query(default=SortType.MOST_RECENT),
    ):
        cached = await cache.get(
            f"jobs/search-{keywords}-{province_ids}-{job_category_ids}-{work_modes}-{work_experiences}-{salary_range_ids}-{page_size}-{page_index}-{sort_type}",
            eviction_group="jobs",
        )

        if cached is not None:
            return json.loads(cached, object_hook=SimpleNamespace)

        result = await handler.handle(
            GetJobsQuery(
                keywords=keywords,
                province_ids=province_ids,
                job_category_ids=job_category_ids,
                work_modes=work_modes,
                work_experiences=work_experiences,
                salary_range_ids=salary_range_ids,
                page_size=page_size,
                page_index=page_index,
                sort_type=sort_type,
            )
        )

        serialized_result = json.dumps(
            result,
            default=serialization_handler,
            ensure_ascii=False,
        )

        await cache.set(
            f"jobs/search-{keywords}-{province_ids}-{job_category_ids}-{work_modes}-{work_experiences}-{salary_range_ids}-{page_size}-{page_index}-{sort_type}",
            serialized_result,
            ttl=300,
            eviction_group="jobs",
        )

        return result

    return router

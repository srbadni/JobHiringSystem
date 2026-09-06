from uuid import UUID
from typing import Annotated, Callable

from fastapi import APIRouter, Depends, Query

from application.jobs_search.dto.company_details import CompanyDetails
from application.jobs_search.handlers.get_company_jobs_handler import GetCompanyJobsHandler
from application.jobs_search.handlers.get_company_details_handler import GetCompanyDetailsHandler
from application.jobs_search.handlers.get_job_details_handler import GetJobDetailsHandler
from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from application.jobs_search.query.get_company_jobs import GetCompanyJobs
from application.jobs_search.query.get_company_details import GetCompanyDetailsQuery
from application.jobs_search.query.get_job_details_query import GetJobDetailsQuery
from application.jobs_search.query.get_jobs import GetJobsQuery
from domain.job_posting.enum import RelevantWorkExperience, WorkMode

JobsResultHandlerProvider = Callable[[], GetJobsQueryHandler]
CompanyJobsResultHandlerProvider = Callable[[], GetCompanyJobsHandler]
CompanyDetailsHandlerProvider = Callable[[], GetCompanyDetailsHandler]
GetJobDetailsHandlerProvider = Callable[[], GetJobDetailsHandler]

def create_jobs_result_router(
    provide_jobs_result_handler: JobsResultHandlerProvider,
    provide_company_jobs_result_handler: CompanyJobsResultHandlerProvider,
    provide_company_details_handler: CompanyDetailsHandlerProvider,
    provide_job_details_handler: GetJobDetailsHandlerProvider,
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

    @router.get("/companies/{company_name}")
    async def get_company_details(  # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[GetCompanyDetailsHandler, Depends(provide_company_details_handler)],
            company_name: str,
    ) -> CompanyDetails:
        query = GetCompanyDetailsQuery(company_en_name=company_name)
        return await query_handler.handle(query=query)

    @router.get("/companies/{company_name}/jobs")
    async def get_company_jobs(  # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[GetCompanyJobsHandler, Depends(provide_company_jobs_result_handler)],
            company_name: str,
    ):
        queries = GetCompanyJobs(
            company_en_name=company_name,
        )
        return await query_handler.handle(query=queries)

    @router.get("/companies/{company_name}/jobs/{job_id}")
    async def get_job_details(  # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[GetJobDetailsHandler, Depends(provide_job_details_handler)],
            company_name: str,
            job_id: UUID,
    ):
        queries = GetJobDetailsQuery(
            job_posting_id=job_id,
            company_en_name=company_name,
        )
        return await query_handler.handle(query=queries)

    return router

from collections.abc import Callable
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends
from application.jobs_search.handlers.get_company_details_handler import GetCompanyDetailsHandler
from application.jobs_search.handlers.get_company_jobs_handler import GetCompanyJobsHandler
from application.jobs_search.handlers.get_job_details_handler import GetJobDetailsHandler
from application.jobs_search.query.get_company_details import GetCompanyDetailsQuery
from application.jobs_search.query.get_company_jobs import GetCompanyJobs
from application.jobs_search.query.get_job_details_query import GetJobDetailsQuery
from .schemas import CompanyRead, JobDetailsRead, JobSearchRead

def create_companies_router(provide_details: Callable[[], GetCompanyDetailsHandler], provide_jobs: Callable[[], GetCompanyJobsHandler], provide_job: Callable[[], GetJobDetailsHandler]) -> APIRouter:
    router = APIRouter(tags=["Applicant - Companies"])
    @router.get("/{company_name}", response_model=CompanyRead)
    async def details(company_name: str, handler: Annotated[GetCompanyDetailsHandler, Depends(provide_details)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(GetCompanyDetailsQuery(company_en_name=company_name))
    @router.get("/{company_name}/jobs", response_model=list[JobSearchRead])
    async def jobs(company_name: str, handler: Annotated[GetCompanyJobsHandler, Depends(provide_jobs)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(GetCompanyJobs(company_en_name=company_name))
    @router.get("/{company_name}/jobs/{job_id}", response_model=JobDetailsRead)
    async def job(company_name: str, job_id: UUID, handler: Annotated[GetJobDetailsHandler, Depends(provide_job)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(GetJobDetailsQuery(job_posting_id=job_id, company_en_name=company_name))
    return router

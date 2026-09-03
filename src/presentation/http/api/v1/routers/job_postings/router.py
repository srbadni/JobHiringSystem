from typing import Annotated, Callable

from fastapi import APIRouter, Depends, status

from application.job_posting.command.create_job_posting import CreateJobPostingCommand
from application.job_posting.handlers.create_job_posting_handler import CreateJobPostingHandler

from .schemas import JobPostingCreate, JobPostingRead

CreateJobPostingHandlerProvider = Callable[[], CreateJobPostingHandler]

def create_job_postings_router(
    provide_create_job_posting_handler: CreateJobPostingHandlerProvider
) -> APIRouter:

    router = APIRouter(tags=["Job Postings"])

    @router.post("", status_code=status.HTTP_201_CREATED, response_model=JobPostingRead)
    async def create_job_posting( # pyright: ignore[reportUnusedFunction]
            job_posting_data: JobPostingCreate,
            command_handler: Annotated[CreateJobPostingHandler, Depends(provide_create_job_posting_handler)]
    ):
        command = CreateJobPostingCommand(
            company_id=job_posting_data.company_id,
            job_category_id=job_posting_data.job_category_id,
            province_id=job_posting_data.province_id,
            city_id=job_posting_data.city_id,
            salary_range_id=job_posting_data.salary_range_id,
            job_title=job_posting_data.job_title,
            job_description=job_posting_data.job_description,
            company_overview=job_posting_data.company_overview,
            is_latin_text=job_posting_data.is_latin_text,
            employment_type=job_posting_data.employment_type,
            work_mode=job_posting_data.work_mode,
            status=job_posting_data.status,
            work_experience=job_posting_data.work_experience,
            minimum_education=job_posting_data.minimum_education,
            gender=job_posting_data.gender,
            military_status=job_posting_data.military_status,
        )
        return await command_handler.handle(command)

    return router
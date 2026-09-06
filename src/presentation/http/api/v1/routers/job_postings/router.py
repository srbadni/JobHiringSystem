from typing import Annotated, Callable
from uuid import UUID

from fastapi import APIRouter, Depends, status

from application.job_posting.command.create_job_posting import CreateJobPostingCommand
from application.job_posting.command.delete_job_posting import DeleteJobPostingCommand
from application.job_posting.command.update_job_posting import UpdateJobPostingCommand
from application.job_posting.handlers.create_job_posting_handler import CreateJobPostingHandler
from application.job_posting.handlers.delete_job_posting_handler import DeleteJobPostingHandler
from application.job_posting.handlers.get_job_posting_by_id_handler import GetJobPostingByIdQueryHandler
from application.job_posting.handlers.list_job_postings_handler import ListJobPostingsQueryHandler
from application.job_posting.handlers.update_job_posting_handler import UpdateJobPostingHandler
from application.job_posting.query.get_job_posting_by_id import GetJobPostingByIdQuery
from application.job_posting.query.list_job_postings import ListJobPostingsQuery

from .schemas import JobPostingCreate, JobPostingRead, JobPostingUpdate

CreateJobPostingHandlerProvider = Callable[[], CreateJobPostingHandler]
ListJobPostingsHandlerProvider = Callable[[], ListJobPostingsQueryHandler]
GetJobPostingByIdHandlerProvider = Callable[[], GetJobPostingByIdQueryHandler]
UpdateJobPostingHandlerProvider = Callable[[], UpdateJobPostingHandler]
DeleteJobPostingHandlerProvider = Callable[[], DeleteJobPostingHandler]

def create_job_postings_router(
    provide_create_job_posting_handler: CreateJobPostingHandlerProvider,
    provide_list_job_postings_handler: ListJobPostingsHandlerProvider,
    provide_get_job_posting_by_id_handler: GetJobPostingByIdHandlerProvider,
    provide_update_job_posting_handler: UpdateJobPostingHandlerProvider,
    provide_delete_job_posting_handler: DeleteJobPostingHandlerProvider,
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

    @router.get("", response_model=list[JobPostingRead])
    async def list_job_postings(  # pyright: ignore[reportUnusedFunction]
            query_handler: Annotated[ListJobPostingsQueryHandler, Depends(provide_list_job_postings_handler)],
    ):
        return await query_handler.handle(ListJobPostingsQuery())

    @router.get("/{job_posting_id}", response_model=JobPostingRead)
    async def get_job_posting(  # pyright: ignore[reportUnusedFunction]
            job_posting_id: UUID,
            query_handler: Annotated[GetJobPostingByIdQueryHandler, Depends(provide_get_job_posting_by_id_handler)],
    ):
        return await query_handler.handle(GetJobPostingByIdQuery(job_posting_id=job_posting_id))

    @router.put("/{job_posting_id}", response_model=JobPostingRead)
    async def update_job_posting(  # pyright: ignore[reportUnusedFunction]
            job_posting_id: UUID,
            job_posting_data: JobPostingUpdate,
            command_handler: Annotated[UpdateJobPostingHandler, Depends(provide_update_job_posting_handler)],
    ):
        command = UpdateJobPostingCommand(
            job_posting_id=job_posting_id,
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

    @router.delete("/{job_posting_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_job_posting(  # pyright: ignore[reportUnusedFunction]
            job_posting_id: UUID,
            command_handler: Annotated[DeleteJobPostingHandler, Depends(provide_delete_job_posting_handler)],
    ) -> None:
        await command_handler.handle(DeleteJobPostingCommand(job_posting_id=job_posting_id))

    return router

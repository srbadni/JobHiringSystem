import uuid
from collections.abc import Callable
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status

from application.authentication.ports.authentication import UserClaims
from application.job_applications.command.create_job_application import CreateJobApplicationCommand
from application.job_applications.handlers.create_job_application_handler import CreateJobApplicationHandler
from application.job_applications.handlers.get_job_application_handler import GetJobApplicationHandler
from application.job_applications.handlers.list_my_job_applications_handler import ListMyJobApplicationsHandler
from application.job_applications.query.get_job_application import GetJobApplicationQuery
from application.job_applications.query.list_my_job_applications import ListMyJobApplicationsQuery
from .schemas import JobApplicationCreate, JobApplicationRead

def create_applications_router(
        provide_create: Callable[[], CreateJobApplicationHandler],
        provide_list: Callable[[], ListMyJobApplicationsHandler],
        provide_get: Callable[[], GetJobApplicationHandler],
        provide_get_current_user: Callable[..., UserClaims]
) -> APIRouter:
    router = APIRouter(tags=["Applicant - Applications"])

    @router.post("/jobs/{job_id}/applications", status_code=status.HTTP_201_CREATED, response_model=JobApplicationRead)
    async def create(job_id: UUID, current_user: Annotated[UserClaims, Depends(provide_get_current_user)], data: JobApplicationCreate, handler: Annotated[CreateJobApplicationHandler, Depends(provide_create)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(CreateJobApplicationCommand(applicant_id=uuid.UUID(current_user["user_id"]), job_posting_id=job_id, folder_id=data.folder_id))

    @router.get("/applications", response_model=list[JobApplicationRead])
    async def list_mine(current_user: Annotated[UserClaims, Depends(provide_get_current_user)], handler: Annotated[ListMyJobApplicationsHandler, Depends(provide_list)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ListMyJobApplicationsQuery(applicant_id=uuid.UUID(current_user["user_id"])))

    @router.get("/applications/{application_id}", response_model=JobApplicationRead)
    async def get(application_id: UUID, current_user: Annotated[UserClaims, Depends(provide_get_current_user)], handler: Annotated[GetJobApplicationHandler, Depends(provide_get)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(GetJobApplicationQuery(application_id=application_id, applicant_id=uuid.UUID(current_user["user_id"])))
    return router

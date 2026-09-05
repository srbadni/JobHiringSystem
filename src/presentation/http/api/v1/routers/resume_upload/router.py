from uuid import UUID
from typing import Annotated, Callable

from fastapi import APIRouter, Depends, File, Form, UploadFile, status

from application.media.command.create_media_command import CreateMediaCommand
from application.media.handler.create_media_handler import CreateMediaHandler

from .schemas import ResumeUploadRead

CreateMediaHandlerProvider = Callable[[], CreateMediaHandler]


def create_resume_upload_router(
    provide_create_media_handler: CreateMediaHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Resumes"])

    @router.post("", status_code=status.HTTP_201_CREATED, response_model=ResumeUploadRead)
    async def upload_resume(  # pyright: ignore[reportUnusedFunction]
        file: Annotated[UploadFile, File(description="Resume file")],
        applicant_profile_id: Annotated[UUID, Form(gt=0)],
        command_handler: Annotated[CreateMediaHandler, Depends(provide_create_media_handler)],
    ) -> ResumeUploadRead:
        media = await command_handler.handle(
            CreateMediaCommand(
                file=file,
                filename=file.filename or "",
                content_type=file.content_type,
                applicant_profile_id=applicant_profile_id,
            )
        )
        return ResumeUploadRead(**media.__dict__)

    return router

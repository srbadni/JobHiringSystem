from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from domain.job_application.exceptions import DuplicateJobApplicationError, JobApplicationNotFoundError
from domain.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from domain.exceptions import ResourceNotFoundError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ResourceNotFoundError)
    @app.exception_handler(UserNotFoundError)
    async def handle_resource_not_found(request: Request, exc: Exception) -> JSONResponse:  # pyright: ignore[reportUnusedFunction]
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})

    @app.exception_handler(UserAlreadyExistsError)
    async def handle_user_conflict(request: Request, exc: UserAlreadyExistsError) -> JSONResponse:  # pyright: ignore[reportUnusedFunction]
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})
    @app.exception_handler(JobApplicationNotFoundError)
    async def handle_job_application_not_found(  # pyright: ignore[reportUnusedFunction]
            request: Request,
            exc: JobApplicationNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)},
        )

    @app.exception_handler(DuplicateJobApplicationError)
    async def handle_duplicate_job_application(  # pyright: ignore[reportUnusedFunction]
            request: Request,
            exc: DuplicateJobApplicationError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)},
        )

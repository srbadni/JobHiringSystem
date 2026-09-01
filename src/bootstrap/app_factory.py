from fastapi import FastAPI

from bootstrap.container import create_user_command_handler
from presentation.http.api.router import router as api_router
from presentation.http.api.v1.routers.users.dependencies import (
    get_create_user_command_handler,
)


def create_app() -> FastAPI:
    """Create and configure the HTTP application."""
    application = FastAPI(title="Job Hiring System")
    application.dependency_overrides[get_create_user_command_handler] = (
        create_user_command_handler
    )
    application.include_router(api_router)
    return application

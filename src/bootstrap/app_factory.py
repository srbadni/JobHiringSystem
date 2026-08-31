from typing import TYPE_CHECKING

from fastapi import FastAPI

from application.users.exceptions import UserAlreadyExistsError
from src.presentation.http.api.router import router as api_router
from src.presentation.http.exception_handlers import user_already_exists_handler

if TYPE_CHECKING:
    from src.bootstrap.container import Container


def create_app(container: "Container | None" = None) -> FastAPI:
    """Create and configure the HTTP application."""
    if container is None:
        from src.bootstrap.container import Container

        container = Container()

    application = FastAPI(title="Job Hiring System")
    application.state.container = container
    application.add_exception_handler(
        UserAlreadyExistsError,
        user_already_exists_handler,
    )
    application.include_router(api_router)
    return application

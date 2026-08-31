from fastapi import FastAPI

from src.presentation.http.api.router import router as api_router


def create_app() -> FastAPI:
    """Create and configure the HTTP application."""
    application = FastAPI(title="Job Hiring System")
    application.include_router(api_router)
    return application

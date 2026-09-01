from fastapi import FastAPI

from bootstrap.providers import provide_create_user_handler
from presentation.http.api.v1.routers.users.router import (
    create_users_router,
)


def create_app() -> FastAPI:
    app = FastAPI(title="Job Hiring System")

    users_router = create_users_router(
        provide_create_user_handler=provide_create_user_handler,
    )

    app.include_router(
        users_router,
        prefix="/api/v1/users",
    )

    return app
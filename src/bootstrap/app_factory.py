from fastapi import FastAPI

from bootstrap.employer_registration_providers import (
    provide_create_employer_and_company_handler,
)
from bootstrap.users_providers import (
    provide_create_user_handler,
    provide_get_all_users_handler,
    provide_get_user_by_email_handler,
    provide_get_user_by_id_handler,
)
from presentation.http.api.v1.routers.users.router import (
    create_users_router,
)
from presentation.http.api.v1.routers.employer.router import create_employer_router


def create_app() -> FastAPI:
    app = FastAPI(title="Job Hiring System")

    users_router = create_users_router(
        provide_create_user_handler=provide_create_user_handler,
        provide_get_all_users_handler=provide_get_all_users_handler,
        provide_get_user_by_id_handler=provide_get_user_by_id_handler,
        provide_get_user_by_email_handler=provide_get_user_by_email_handler,
    )

    employer_router = create_employer_router(
        provide_create_employer_and_company_handler=provide_create_employer_and_company_handler,
    )

    app.include_router(
        users_router,
        prefix="/api/v1/users",
    )

    app.include_router(
        employer_router,
        prefix="/api/v1/employers",
    )

    return app

from application.employer_registration.handlers.create_employer_handler import (
    CreateEmployerHandler,
)
from bootstrap.common_providers import password_hasher, provide_uow


def provide_create_employer_and_company_handler() -> CreateEmployerHandler:
    return CreateEmployerHandler(
        uow=provide_uow(),
        hasher=password_hasher,
    )

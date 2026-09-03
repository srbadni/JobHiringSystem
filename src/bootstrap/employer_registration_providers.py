from application.employer_registration.handlers.create_employer_and_company_handler import (
    CreateEmployerAndCompanyHandler,
)
from bootstrap.common_providers import password_hasher, provide_uow


def provide_create_employer_and_company_handler() -> CreateEmployerAndCompanyHandler:
    return CreateEmployerAndCompanyHandler(
        uow=provide_uow(),
        hasher=password_hasher,
    )

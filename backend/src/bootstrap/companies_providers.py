from application.companies.handlers.create_company_handler import CreateCompanyHandler
from bootstrap.common_providers import provide_uow


def provide_add_company_handler() -> CreateCompanyHandler:
    return CreateCompanyHandler(
        uow=provide_uow()
    )
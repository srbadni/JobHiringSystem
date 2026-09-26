from typing import Annotated, Callable

from fastapi import APIRouter, Depends, status

from application.employer_registration.handlers.create_employer_handler import \
    CreateEmployerHandler
from application.users.command.create_user import CreateUserCommand
from application.companies.command.create_company import CreateCompanyCommand
from application.employer_registration.command.create_employer_and_company import CreateEmployerAndCompany

from .schemas import EmployerCompanyCreate, EmployerRead

CreateEmployerAndCompanyHandlerProvider = Callable[[], CreateEmployerHandler]


def create_employer_router(
        provide_create_employer_and_company_handler: CreateEmployerAndCompanyHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Employer"])

    @router.post("/register", status_code=status.HTTP_201_CREATED, response_model=EmployerRead)
    async def create_employer_and_company(  # pyright: ignore[reportUnusedFunction]
            employer_company_data: EmployerCompanyCreate,
            command_handler: Annotated[
                CreateEmployerHandler, Depends(provide_create_employer_and_company_handler)]
    ):
        user_command = CreateUserCommand(
            full_name=employer_company_data.employer.full_name,
            phone_number=employer_company_data.employer.phone_number,
            email=employer_company_data.employer.email,
            password=employer_company_data.employer.password,
            profile_image_url=employer_company_data.employer.profile_image_url,
        )
        company_command = CreateCompanyCommand(
            name=employer_company_data.company.name,
            persian_name=employer_company_data.company.persian_name,
            phone_number=employer_company_data.company.phone_number,
            province_id=employer_company_data.company.province_id,
            city_id=employer_company_data.company.city_id,
            activity_id=employer_company_data.company.activity_id,
            personnel_count=employer_company_data.company.personnel_count,
            logo_path=employer_company_data.company.logo_path,
            description=employer_company_data.company.description,
            website=employer_company_data.company.website,
        )
        command = CreateEmployerAndCompany(
            employer=user_command,
            company=company_command,
        )
        created_employer = await command_handler.handle(command=command)
        return EmployerRead(
            full_name=created_employer.full_name,
            phone_number=created_employer.phone_number,
            email=created_employer.email,
            profile_image_url=created_employer.profile_image_url,
        )

    return router

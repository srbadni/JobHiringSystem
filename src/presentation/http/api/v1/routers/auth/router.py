from collections.abc import Callable
from typing import Annotated
from fastapi import APIRouter, Depends, status
from application.users.command.create_user import CreateUserCommand
from application.users.handlers import CreateUserCommandHandler
from application.employer_registration.command.create_employer_and_company import CreateEmployerAndCompany
from application.employer_registration.handlers.create_employer_and_company_handler import CreateEmployerAndCompanyHandler
from application.companies.command.create_company import CreateCompanyCommand
from domain.user.enums import UserType
from presentation.http.api.v1.routers.users.schemas import UserCreate, UserRead
from presentation.http.api.v1.routers.employer.schemas import EmployerCompanyCreate, EmployerRead


def create_auth_router(
    provide_create_user_handler: Callable[[], CreateUserCommandHandler],
    provide_create_employer_handler: Callable[[], CreateEmployerAndCompanyHandler],
) -> APIRouter:
    router = APIRouter(tags=["Authentication"])

    @router.post("/register/applicant", status_code=status.HTTP_201_CREATED, response_model=UserRead)
    async def register_applicant(data: UserCreate, handler: Annotated[CreateUserCommandHandler, Depends(provide_create_user_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(CreateUserCommand(
            full_name=data.full_name, phone_number=data.phone_number, email=data.email,
            password=data.password, profile_image_url=data.profile_image_url,
            user_type=UserType.APPLICANT,
        ))

    @router.post("/register/employer", status_code=status.HTTP_201_CREATED, response_model=EmployerRead)
    async def register_employer(data: EmployerCompanyCreate, handler: Annotated[CreateEmployerAndCompanyHandler, Depends(provide_create_employer_handler)]):  # pyright: ignore[reportUnusedFunction]
        employer = data.employer
        company = data.company
        command = CreateEmployerAndCompany(
            employer=CreateUserCommand(full_name=employer.full_name, phone_number=employer.phone_number,
                email=employer.email, password=employer.password, profile_image_url=employer.profile_image_url,
                user_type=UserType.EMPLOYER),
            company=CreateCompanyCommand(**company.model_dump()),
        )
        return await handler.handle(command)
    return router

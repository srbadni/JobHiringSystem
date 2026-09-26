from collections.abc import Callable
from typing import Annotated
from fastapi import APIRouter, Depends, status, Header, HTTPException
from fastapi.security import HTTPBearer

from application.authentication.command.applicant_login import ApplicantLoginCommand
from application.authentication.command.employer_login import EmployerLoginCommand
from application.authentication.exceptions import UserNotFound, IncorrectPassword
from application.authentication.handler.employer_login_handler import EmployerLoginHandler
from application.authentication.handler.get_current_user_handler import GetCurrentUserHandler
from application.authentication.handler.applicant_login_handler import ApplicantLoginHandler
from application.authentication.query.get_current_user import GetCurrentUserQuery
from application.companies.handlers.create_company_handler import CreateCompanyHandler
from application.users.command.create_user import CreateUserCommand
from application.users.handlers import CreateUserCommandHandler
from application.employer_registration.command.create_employer_and_company import CreateEmployerAndCompany
from application.employer_registration.handlers.create_employer_handler import CreateEmployerHandler
from application.companies.command.create_company import CreateCompanyCommand
from domain.user.enums import UserType
from presentation.http.api.v1.routers.users.schemas import UserCreate, UserRead, LoginModel
from presentation.http.api.v1.routers.employer.schemas import EmployerRead, EmployerCreate, CompanyRead, CompanyCreate

security = HTTPBearer()

def create_auth_router(
    provide_create_user_handler: Callable[[], CreateUserCommandHandler],
    provide_create_employer_handler: Callable[[], CreateEmployerHandler],
    provide_get_current_user_handler: Callable[[], GetCurrentUserHandler],
    provide_login_handler: Callable[[], ApplicantLoginHandler],
    provide_employer_login_handler: Callable[[], EmployerLoginHandler],
    provide_add_company_handler: Callable[[], CreateCompanyHandler],
) -> APIRouter:
    router = APIRouter(tags=["Authentication"])

    @router.post("/login", status_code=status.HTTP_200_OK)
    async def login(data: LoginModel, handler: Annotated[
        ApplicantLoginHandler, Depends(provide_login_handler)]):  # pyright: ignore[reportUnusedFunction]
        try:
            return await handler.handle(ApplicantLoginCommand(
                email=data.email,
                password=data.password,
            ))
        except UserNotFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        except IncorrectPassword:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password")

    @router.post("/employer-login", status_code=status.HTTP_200_OK)
    async def login(data: LoginModel, handler: Annotated[
        EmployerLoginHandler, Depends(provide_employer_login_handler)]):  # pyright: ignore[reportUnusedFunction]
        try:
            return await handler.handle(EmployerLoginCommand(
                email=data.email,
                password=data.password,
            ))
        except UserNotFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        except IncorrectPassword:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password")

    @router.get("/users/me", status_code=status.HTTP_200_OK)
    async def get_me(
            handler: Annotated[
                GetCurrentUserHandler, Depends(provide_get_current_user_handler)],
            credentials = Depends(security),
    ):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(GetCurrentUserQuery(
            access_token=credentials.credentials
        ))

    @router.post("/register/applicant", status_code=status.HTTP_201_CREATED, response_model=UserRead)
    async def register_applicant(data: UserCreate, handler: Annotated[CreateUserCommandHandler, Depends(provide_create_user_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(CreateUserCommand(
            full_name=data.full_name, phone_number=data.phone_number, email=data.email,
            password=data.password, profile_image_url=data.profile_image_url,
            user_type=UserType.APPLICANT,
        ))

    @router.post("/register/employer", status_code=status.HTTP_201_CREATED, response_model=EmployerRead)
    async def register_employer(employer: EmployerCreate, handler: Annotated[CreateEmployerHandler, Depends(provide_create_employer_handler)]):  # pyright: ignore[reportUnusedFunction]
        command = CreateUserCommand(
            full_name=employer.full_name,
            phone_number=employer.phone_number,
            email=employer.email,
            password=employer.password,
            profile_image_url=employer.profile_image_url,
            user_type=UserType.EMPLOYER,
        )
        return await handler.handle(command)

    @router.post("/register/company", status_code=status.HTTP_201_CREATED, response_model=CompanyRead)
    async def register_company(company: CompanyCreate, handler: Annotated[
        CreateCompanyHandler, Depends(provide_add_company_handler)]):  # pyright: ignore[reportUnusedFunction]
        command = CreateCompanyCommand(
            name=company.name,
            persian_name=company.persian_name,
            phone_number=company.phone_number,
            province_id=company.province_id,
            city_id=company.city_id,
            activity_id=company.activity_id,
            personnel_count=company.personnel_count,
            logo_path=company.logo_path,
            description=company.description,
            website=company.website,
        )
        return await handler.handle(command)
    return router

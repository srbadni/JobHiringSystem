from collections.abc import Callable
from typing import Annotated
from fastapi import APIRouter, Depends, status, Header
from fastapi.security import HTTPBearer

from application.authentication.command.login import LoginCommand
from application.authentication.handler.get_current_user_handler import GetCurrentUserHandler
from application.authentication.handler.login_handler import LoginHandler
from application.authentication.query.get_current_user import GetCurrentUserQuery
from application.users.command.create_user import CreateUserCommand
from application.users.handlers import CreateUserCommandHandler
from application.employer_registration.command.create_employer_and_company import CreateEmployerAndCompany
from application.employer_registration.handlers.create_employer_and_company_handler import CreateEmployerAndCompanyHandler
from application.companies.command.create_company import CreateCompanyCommand
from domain.user.enums import UserType
from presentation.http.api.v1.routers.users.schemas import UserCreate, UserRead, LoginModel
from presentation.http.api.v1.routers.employer.schemas import EmployerCompanyCreate, EmployerRead

security = HTTPBearer()

def create_auth_router(
    provide_create_user_handler: Callable[[], CreateUserCommandHandler],
    provide_create_employer_handler: Callable[[], CreateEmployerAndCompanyHandler],
    provide_get_current_user_handler: Callable[[], GetCurrentUserHandler],
    provide_login_handler: Callable[[], LoginHandler],
) -> APIRouter:
    router = APIRouter(tags=["Authentication"])

    @router.post("/login", status_code=status.HTTP_200_OK)
    async def login(data: LoginModel, handler: Annotated[
        LoginHandler, Depends(provide_login_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(LoginCommand(
            email=data.email,
            password=data.password,
        ))

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

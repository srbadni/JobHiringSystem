from application.common.ports.unit_of_work import UnitOfWork
from application.users.handlers import ListUsersQueryHandler, CreateUserCommandHandler, GetUserByIdQueryHandler, \
    GetUserByEmailQueryHandler
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal
from infrastructure.persistence.sqlalchemy.unit_of_work import (
    SqlAlchemyUnitOfWork,
)
from infrastructure.security.pwdlib_password_hasher import (
    PwdlibPasswordHasher,
)
from application.employer_registration.handlers.create_employer_and_company_handler import CreateEmployerAndCompanyHandler


password_hasher = PwdlibPasswordHasher()


def provide_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(
        session_factory=AsyncSessionLocal,
    )


def provide_create_user_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(
        uow=provide_uow(),
        hasher=password_hasher,
    )

def provide_get_all_users_handler() -> ListUsersQueryHandler:
    return ListUsersQueryHandler(
        uow=provide_uow(),
    )

def provide_get_user_by_id_handler() -> GetUserByIdQueryHandler:
    return GetUserByIdQueryHandler(
        uow=provide_uow(),
    )

def provide_get_user_by_email_handler() -> GetUserByEmailQueryHandler:
    return GetUserByEmailQueryHandler(
        uow=provide_uow(),
    )

def provide_create_employer_and_company_handler() -> CreateEmployerAndCompanyHandler:
    return CreateEmployerAndCompanyHandler(
        uow=provide_uow(),
        hasher=password_hasher,
    )
from domain.company.models import Company
from domain.user.models import User
from domain.user.enums import UserType
from domain.company_membership.models import CompanyMembership

from ..command.create_employer_and_company import CreateEmployerAndCompany
from ...common.ports.password_hasher import PasswordHasher
from ...common.ports.unit_of_work import UnitOfWork
from domain.user.exceptions import UserAlreadyExistsError
from ...users.command.create_user import CreateUserCommand


class CreateEmployerHandler:
    def __init__(self, uow: UnitOfWork, hasher: PasswordHasher) -> None:
        self.uow = uow
        self.hasher = hasher

    async def handle(self, command: CreateUserCommand) -> User:
        async with self.uow:
            if await self.uow.users.exists_by_email(command.email):
                raise UserAlreadyExistsError("A user with this email already exists.")
            hashed_password = self.hasher.hash(command.password)
            user_domain = User(
                full_name=command.full_name,
                phone_number=command.phone_number,
                email=command.email,
                profile_image_url=command.profile_image_url,
                hashed_password=hashed_password,
                user_type=UserType.EMPLOYER,
            )
            created_employer = await self.uow.users.add(user_domain)
            await self.uow.commit()
            return created_employer

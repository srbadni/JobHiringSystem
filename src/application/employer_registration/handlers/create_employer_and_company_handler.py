from domain.company.models import Company
from domain.user.models import User
from domain.user.enums import UserType
from domain.company_membership.models import CompanyMembership

from ..command.create_employer_and_company import CreateEmployerAndCompany
from ...common.ports.password_hasher import PasswordHasher
from ...common.ports.unit_of_work import UnitOfWork


class CreateEmployerAndCompanyHandler:
    def __init__(self, uow: UnitOfWork, hasher: PasswordHasher) -> None:
        self.uow = uow
        self.hasher = hasher

    async def handle(self, command: CreateEmployerAndCompany) -> User:
        async with self.uow:
            hashed_password = self.hasher.hash(command.employer.password)
            user_domain = User(
                full_name=command.employer.full_name,
                phone_number=command.employer.phone_number,
                email=command.employer.email,
                profile_image_url=command.employer.profile_image_url,
                hashed_password=hashed_password,
                user_type=UserType.EMPLOYER,
            )
            company_domain = Company(
                name=command.company.name,
                persian_name=command.company.persian_name,
                phone_number=command.company.phone_number,
                province_id=command.company.province_id,
                city_id=command.company.city_id,
                activity_id=command.company.activity_id,
                personnel_count=command.company.personnel_count,
                logo_path=command.company.logo_path,
                description=command.company.description,
                website=command.company.website,
            )
            created_employer = await self.uow.users.add(user_domain)
            created_company = await self.uow.companies.add(company_domain)
            await self.uow.company_memberships.add(CompanyMembership(
                user_id=created_employer.id,
                company_id=created_company.id,
                is_admin=True,
            ))
            await self.uow.commit()
            return created_employer

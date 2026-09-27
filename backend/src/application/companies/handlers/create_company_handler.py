from domain.company.models import Company
from ...common.ports.unit_of_work import UnitOfWork

from ..command.create_company import CreateCompanyCommand


class CreateCompanyHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateCompanyCommand) -> Company:
        async with self.uow:
            company_domain = Company(
                name=command.name,
                persian_name=command.persian_name,
                phone_number=command.phone_number,
                province_id=command.province_id,
                city_id=command.city_id,
                activity_id=command.activity_id,
                personnel_count=command.personnel_count,
                logo_path=command.logo_path,
                description=command.description,
                website=command.website,
            )

            return await self.uow.companies.add(company_domain)
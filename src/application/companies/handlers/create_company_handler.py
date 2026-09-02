from domain.company.models import Company

from ...companies.ports.repositories.company_repository import CompanyRepository

from ..command.create_company import CreateCompanyCommand


class CreateCompanyHandler:
    def __init__(self, repository: CompanyRepository) -> None:
        self.repository = repository

    async def handle(self, command: CreateCompanyCommand) -> Company:
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

        return await self.repository.add(company_domain)
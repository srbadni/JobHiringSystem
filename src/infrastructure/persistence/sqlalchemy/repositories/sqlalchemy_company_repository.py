from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.companies.ports.repositories.company_repository import CompanyRepository
from domain.company.models import Company as DomainCompany
from ..models.company import Company as CompanyModel


class SQLAlchemyCompanyRepository(CompanyRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _to_domain(company_orm_model: CompanyModel) -> DomainCompany:
        return DomainCompany(
            id=company_orm_model.id,
            name=company_orm_model.name,
            persian_name=company_orm_model.persian_name,
            province_id=company_orm_model.province_id,
            city_id=company_orm_model.city_id,
            activity_id=company_orm_model.activity_id,
            personnel_count=company_orm_model.personnel_count,
            logo_path=company_orm_model.logo_path,
            phone_number=company_orm_model.phone_number,
            description=company_orm_model.description,
            website=company_orm_model.website,
        )

    @staticmethod
    def _to_orm_model(company: DomainCompany) -> CompanyModel:
        return CompanyModel(
            id=company.id,
            name=company.name,
            persian_name=company.persian_name,
            province_id=company.province_id,
            city_id=company.city_id,
            activity_id=company.activity_id,
            personnel_count=company.personnel_count,
            logo_path=company.logo_path,
            phone_number=company.phone_number,
            description=company.description,
            website=company.website,
        )

    async def add(self, company: DomainCompany) -> DomainCompany:
        mapped_company = self._to_orm_model(company=company)
        self.session.add(mapped_company)
        await self.session.flush()
        return self._to_domain(company_orm_model=mapped_company)


    async def get(self, company_id: UUID) -> DomainCompany:
        stmt = select(CompanyModel).where(
            CompanyModel.id == company_id
        )

        result = await self.session.execute(stmt)
        company_from_db = result.scalar_one_or_none()

        if company_from_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )

        return self._to_domain(company_from_db)
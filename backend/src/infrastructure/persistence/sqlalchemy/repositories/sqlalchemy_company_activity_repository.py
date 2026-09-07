from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.company_activities.ports.company_activity_repository import CompanyActivityRepository
from domain.company_activity.models import CompanyActivity
from ..models.company_activity import CompanyActivity as CompanyActivityORMModel


class SqlAlchemyCompanyActivityRepository(CompanyActivityRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def _to_domain(model: CompanyActivityORMModel) -> CompanyActivity:
        return CompanyActivity(
            code=model.code,
            title=model.title,
            id=model.id,
        )

    async def list(self) -> list[CompanyActivity]:
        result = await self.session.scalars(select(CompanyActivityORMModel))
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, company_activity_id: UUID) -> CompanyActivity:
        model = await self.session.get_one(CompanyActivityORMModel, company_activity_id)
        return self._to_domain(model)

    async def add(self, company_activity: CompanyActivity) -> CompanyActivity:
        model = CompanyActivityORMModel(
            code=company_activity.code,
            title=company_activity.title,
        )
        self.session.add(model)
        await self.session.flush()
        return self._to_domain(model)

    async def update(self, company_activity: CompanyActivity) -> CompanyActivity:
        model = await self.session.get_one(CompanyActivityORMModel, company_activity.id)
        model.code = company_activity.code
        model.title = company_activity.title
        await self.session.flush()
        return self._to_domain(model)

    async def delete(self, company_activity_id: UUID) -> None:
        model = await self.session.get_one(CompanyActivityORMModel, company_activity_id)
        await self.session.delete(model)
        await self.session.flush()

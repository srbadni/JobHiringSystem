from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.salary_ranges.ports.salary_range_repository import SalaryRangeRepository
from domain.salary_range.models import SalaryRange
from ..models.salary_range import SalaryRange as SalaryRangeORMModel


class SqlAlchemySalaryRangeRepository(SalaryRangeRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def _to_domain(model: SalaryRangeORMModel) -> SalaryRange:
        return SalaryRange(
            title=model.title,
            min_salary=model.min_salary,
            max_salary=model.max_salary,
            id=model.id,
        )

    async def list(self) -> list[SalaryRange]:
        result = await self.session.scalars(select(SalaryRangeORMModel))
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, salary_range_id: UUID) -> SalaryRange:
        model = await self.session.get_one(SalaryRangeORMModel, salary_range_id)
        return self._to_domain(model)

    async def add(self, salary_range: SalaryRange) -> SalaryRange:
        model = SalaryRangeORMModel(
            title=salary_range.title,
            min_salary=salary_range.min_salary,
            max_salary=salary_range.max_salary,
        )
        self.session.add(model)
        await self.session.flush()
        return self._to_domain(model)

    async def update(self, salary_range: SalaryRange) -> SalaryRange:
        model = await self.session.get_one(SalaryRangeORMModel, salary_range.id)
        model.title = salary_range.title
        model.min_salary = salary_range.min_salary
        model.max_salary = salary_range.max_salary
        await self.session.flush()
        return self._to_domain(model)

    async def delete(self, salary_range_id: UUID) -> None:
        model = await self.session.get_one(SalaryRangeORMModel, salary_range_id)
        await self.session.delete(model)
        await self.session.flush()

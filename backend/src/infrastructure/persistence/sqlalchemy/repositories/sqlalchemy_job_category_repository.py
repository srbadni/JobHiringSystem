from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.job_categories.ports.job_category_repository import JobCategoryRepository
from domain.job_category.models import JobCategory
from ..models.job_categories import JobCategory as JobCategoryORMModel


class SqlAlchemyJobCategoryRepository(JobCategoryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def _to_domain(model: JobCategoryORMModel) -> JobCategory:
        return JobCategory(
            code=model.code,
            title=model.title,
            id=model.id,
        )

    async def list(self) -> list[JobCategory]:
        result = await self.session.scalars(select(JobCategoryORMModel))
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, job_category_id: UUID) -> JobCategory:
        model = await self.session.get_one(JobCategoryORMModel, job_category_id)
        return self._to_domain(model)

    async def add(self, job_category: JobCategory) -> JobCategory:
        model = JobCategoryORMModel(
            code=job_category.code,
            title=job_category.title,
        )
        self.session.add(model)
        await self.session.flush()
        return self._to_domain(model)

    async def update(self, job_category: JobCategory) -> JobCategory:
        model = await self.session.get_one(JobCategoryORMModel, job_category.id)
        model.code = job_category.code
        model.title = job_category.title
        await self.session.flush()
        return self._to_domain(model)

    async def delete(self, job_category_id: UUID) -> None:
        model = await self.session.get_one(JobCategoryORMModel, job_category_id)
        await self.session.delete(model)
        await self.session.flush()

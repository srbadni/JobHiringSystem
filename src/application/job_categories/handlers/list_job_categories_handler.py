from application.common.ports.unit_of_work import UnitOfWork
from domain.job_category.models import JobCategory

from ..query.list_job_categories import ListJobCategoriesQuery


class ListJobCategoriesQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListJobCategoriesQuery) -> list[JobCategory]:
        async with self.uow:
            return await self.uow.job_categories.list()

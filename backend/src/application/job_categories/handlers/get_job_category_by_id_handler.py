from application.common.ports.unit_of_work import UnitOfWork
from domain.job_category.models import JobCategory

from ..query.get_job_category_by_id import GetJobCategoryByIdQuery


class GetJobCategoryByIdQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetJobCategoryByIdQuery) -> JobCategory:
        async with self.uow:
            return await self.uow.job_categories.get_by_id(query.job_category_id)

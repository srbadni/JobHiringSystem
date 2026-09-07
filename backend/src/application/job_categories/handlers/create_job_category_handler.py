from application.common.ports.unit_of_work import UnitOfWork
from domain.job_category.models import JobCategory

from ..command.create_job_category import CreateJobCategoryCommand


class CreateJobCategoryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateJobCategoryCommand) -> JobCategory:
        async with self.uow:
            entity = JobCategory(
                code=command.code,
                title=command.title,
            )
            result = await self.uow.job_categories.add(entity)
            await self.uow.commit()
            return result

from application.common.ports.unit_of_work import UnitOfWork
from domain.job_category.models import JobCategory

from ..command.update_job_category import UpdateJobCategoryCommand


class UpdateJobCategoryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: UpdateJobCategoryCommand) -> JobCategory:
        async with self.uow:
            entity = JobCategory(
                id=command.job_category_id,
            code=command.code,
            title=command.title,
            )
            result = await self.uow.job_categories.update(entity)
            await self.uow.commit()
            return result

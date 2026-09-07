from application.common.ports.unit_of_work import UnitOfWork

from ..command.delete_job_category import DeleteJobCategoryCommand


class DeleteJobCategoryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: DeleteJobCategoryCommand) -> None:
        async with self.uow:
            await self.uow.job_categories.delete(command.job_category_id)
            await self.uow.commit()

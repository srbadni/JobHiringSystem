from application.common.ports.unit_of_work import UnitOfWork

from ..command.delete_salary_range import DeleteSalaryRangeCommand


class DeleteSalaryRangeHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: DeleteSalaryRangeCommand) -> None:
        async with self.uow:
            await self.uow.salary_ranges.delete(command.salary_range_id)
            await self.uow.commit()

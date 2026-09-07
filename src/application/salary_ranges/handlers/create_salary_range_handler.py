from application.common.ports.unit_of_work import UnitOfWork
from domain.salary_range.models import SalaryRange

from ..command.create_salary_range import CreateSalaryRangeCommand


class CreateSalaryRangeHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateSalaryRangeCommand) -> SalaryRange:
        async with self.uow:
            entity = SalaryRange(
                title=command.title,
                min_salary=command.min_salary,
                max_salary=command.max_salary,
            )
            result = await self.uow.salary_ranges.add(entity)
            await self.uow.commit()
            return result

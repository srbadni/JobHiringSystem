from application.common.ports.unit_of_work import UnitOfWork
from domain.salary_range.models import SalaryRange

from ..command.update_salary_range import UpdateSalaryRangeCommand


class UpdateSalaryRangeHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: UpdateSalaryRangeCommand) -> SalaryRange:
        async with self.uow:
            entity = SalaryRange(
                id=command.salary_range_id,
            title=command.title,
            min_salary=command.min_salary,
            max_salary=command.max_salary,
            )
            result = await self.uow.salary_ranges.update(entity)
            await self.uow.commit()
            return result

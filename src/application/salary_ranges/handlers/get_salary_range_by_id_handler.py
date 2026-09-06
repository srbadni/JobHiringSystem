from application.common.ports.unit_of_work import UnitOfWork
from domain.salary_range.models import SalaryRange

from ..query.get_salary_range_by_id import GetSalaryRangeByIdQuery


class GetSalaryRangeByIdQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetSalaryRangeByIdQuery) -> SalaryRange:
        async with self.uow:
            return await self.uow.salary_ranges.get_by_id(query.salary_range_id)

from application.common.ports.unit_of_work import UnitOfWork
from domain.salary_range.models import SalaryRange

from ..query.list_salary_ranges import ListSalaryRangesQuery


class ListSalaryRangesQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListSalaryRangesQuery) -> list[SalaryRange]:
        async with self.uow:
            return await self.uow.salary_ranges.list()

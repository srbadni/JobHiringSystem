from application.common.ports.unit_of_work import UnitOfWork
from domain.location.models import Province

from ..query.list_provinces import ListProvincesQuery


class ListProvincesQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListProvincesQuery) -> list[Province]:
        async with self.uow:
            return await self.uow.locations.list_provinces()

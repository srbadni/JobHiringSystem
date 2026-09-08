from application.common.ports.unit_of_work import UnitOfWork
from domain.location.models import City

from ..query.list_cities import ListCitiesQuery


class ListCitiesQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListCitiesQuery) -> list[City]:
        async with self.uow:
            return await self.uow.locations.list_cities(query.province_id)

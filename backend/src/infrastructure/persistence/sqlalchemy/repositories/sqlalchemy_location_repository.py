from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.locations.ports.location_repository import LocationRepository
from domain.location.models import City, Province

from ..models.city import City as CityORMModel
from ..models.province import Province as ProvinceORMModel


class SqlAlchemyLocationRepository(LocationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list_provinces(self) -> list[Province]:
        statement = select(ProvinceORMModel).order_by(ProvinceORMModel.name)
        result = await self.session.scalars(statement)
        return [
            Province(id=model.id, name=model.name, english_name=model.english_name)
            for model in result.all()
        ]

    async def list_cities(self, province_id: UUID | None = None) -> list[City]:
        statement = select(CityORMModel)
        if province_id is not None:
            statement = statement.where(CityORMModel.province_id == province_id)
        statement = statement.order_by(CityORMModel.name)
        result = await self.session.scalars(statement)
        return [
            City(
                id=model.id,
                name=model.name,
                english_name=model.english_name,
                province_id=model.province_id,
            )
            for model in result.all()
        ]

from abc import ABC, abstractmethod
from uuid import UUID

from domain.location.models import City, Province


class LocationRepository(ABC):
    @abstractmethod
    async def list_provinces(self) -> list[Province]:
        pass

    @abstractmethod
    async def list_cities(self, province_id: UUID | None = None) -> list[City]:
        pass

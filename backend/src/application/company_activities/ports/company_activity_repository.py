from abc import ABC, abstractmethod
from uuid import UUID

from domain.company_activity.models import CompanyActivity


class CompanyActivityRepository(ABC):
    @abstractmethod
    async def list(self) -> list[CompanyActivity]:
        pass

    @abstractmethod
    async def get_by_id(self, company_activity_id: UUID) -> CompanyActivity:
        pass

    @abstractmethod
    async def add(self, company_activity: CompanyActivity) -> CompanyActivity:
        pass

    @abstractmethod
    async def update(self, company_activity: CompanyActivity) -> CompanyActivity:
        pass

    @abstractmethod
    async def delete(self, company_activity_id: UUID) -> None:
        pass

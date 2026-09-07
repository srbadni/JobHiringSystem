from abc import ABC, abstractmethod
from uuid import UUID

from domain.salary_range.models import SalaryRange


class SalaryRangeRepository(ABC):
    @abstractmethod
    async def list(self) -> list[SalaryRange]:
        pass

    @abstractmethod
    async def get_by_id(self, salary_range_id: UUID) -> SalaryRange:
        pass

    @abstractmethod
    async def add(self, salary_range: SalaryRange) -> SalaryRange:
        pass

    @abstractmethod
    async def update(self, salary_range: SalaryRange) -> SalaryRange:
        pass

    @abstractmethod
    async def delete(self, salary_range_id: UUID) -> None:
        pass

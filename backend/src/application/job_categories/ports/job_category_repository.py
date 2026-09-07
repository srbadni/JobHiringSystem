from abc import ABC, abstractmethod
from uuid import UUID

from domain.job_category.models import JobCategory


class JobCategoryRepository(ABC):
    @abstractmethod
    async def list(self) -> list[JobCategory]:
        pass

    @abstractmethod
    async def get_by_id(self, job_category_id: UUID) -> JobCategory:
        pass

    @abstractmethod
    async def add(self, job_category: JobCategory) -> JobCategory:
        pass

    @abstractmethod
    async def update(self, job_category: JobCategory) -> JobCategory:
        pass

    @abstractmethod
    async def delete(self, job_category_id: UUID) -> None:
        pass

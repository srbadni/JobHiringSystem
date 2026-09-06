from abc import ABC, abstractmethod
from uuid import UUID

from domain.job_posting.models import JobPosting


class JobPostingRepository(ABC):

    @abstractmethod
    async def list(self) -> list[JobPosting]:
        pass

    @abstractmethod
    async def get_by_id(self, job_posting_id: UUID) -> JobPosting:
        pass

    @abstractmethod
    async def add(self, job_posting: JobPosting) -> JobPosting:
        pass

    @abstractmethod
    async def update(self, job_posting: JobPosting) -> JobPosting:
        pass

    @abstractmethod
    async def delete(self, job_posting_id: UUID) -> None:
        pass

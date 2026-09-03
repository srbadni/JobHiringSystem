from abc import ABC, abstractmethod

from domain.job_posting.models import JobPosting


class JobPostingRepository(ABC):

    @abstractmethod
    async def add(self, job_posting: JobPosting) -> JobPosting:
        pass
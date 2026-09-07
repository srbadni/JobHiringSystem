from abc import ABC, abstractmethod
from uuid import UUID

from domain.job_application.models import JobApplication


class JobApplicationRepository(ABC):
    @abstractmethod
    async def add(self, application: JobApplication, company_name: str) -> JobApplication:
        pass

    @abstractmethod
    async def list_by_applicant(self, applicant_id: UUID) -> list[JobApplication]:
        pass

    @abstractmethod
    async def get_by_id(self, application_id: UUID) -> JobApplication:
        pass

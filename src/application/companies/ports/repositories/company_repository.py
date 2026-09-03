from abc import ABC, abstractmethod
from uuid import UUID

from domain.company.models import Company


class CompanyRepository(ABC):

    @abstractmethod
    async def add(self, company: Company) -> Company:
        pass

    @abstractmethod
    async def get(self, company_id: UUID) -> Company:
        pass
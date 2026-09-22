from abc import ABC, abstractmethod
from uuid import UUID

from domain.company_membership.models import CompanyMembership


class CompanyMembershipRepository(ABC):

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> CompanyMembership | None:
        pass

    @abstractmethod
    async def add(self, company_membership: CompanyMembership) -> CompanyMembership:
        pass
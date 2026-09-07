from abc import ABC, abstractmethod

from domain.company_membership.models import CompanyMembership


class CompanyMembershipRepository(ABC):

    @abstractmethod
    async def add(self, company_membership: CompanyMembership) -> CompanyMembership:
        pass
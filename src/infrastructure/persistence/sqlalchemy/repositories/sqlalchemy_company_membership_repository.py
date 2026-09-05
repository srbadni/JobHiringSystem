from sqlalchemy.ext.asyncio import AsyncSession

from application.company_membership.ports.company_membership_repository import CompanyMembershipRepository
from domain.company_membership.models import CompanyMembership
from infrastructure.persistence.sqlalchemy.models.company_membership import CompanyMembership as CompanyMembershipORMModel


class SqlAlchemyCompanyMembershipRepository(CompanyMembershipRepository):

    @staticmethod
    def _to_domain(model: CompanyMembershipORMModel) -> CompanyMembership:
        return CompanyMembership(
            id=model.id,
            user_id=model.user_id,
            company_id=model.company_id,
            is_admin=model.is_admin,
        )


    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, company_membership: CompanyMembership) -> CompanyMembership:

        company_membership_orm_model = CompanyMembershipORMModel(
            id=company_membership.id,
            user_id=company_membership.user_id,
            company_id=company_membership.company_id,
            is_admin=company_membership.is_admin,
        )

        self.session.add(company_membership_orm_model)
        return self._to_domain(company_membership_orm_model)
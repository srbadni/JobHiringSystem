from application.common.ports.unit_of_work import UnitOfWork
from domain.company_activity.models import CompanyActivity

from ..query.get_company_activity_by_id import GetCompanyActivityByIdQuery


class GetCompanyActivityByIdQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetCompanyActivityByIdQuery) -> CompanyActivity:
        async with self.uow:
            return await self.uow.company_activities.get_by_id(query.company_activity_id)

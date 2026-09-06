from application.common.ports.unit_of_work import UnitOfWork
from domain.company_activity.models import CompanyActivity

from ..query.list_company_activities import ListCompanyActivitiesQuery


class ListCompanyActivitiesQueryHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListCompanyActivitiesQuery) -> list[CompanyActivity]:
        async with self.uow:
            return await self.uow.company_activities.list()

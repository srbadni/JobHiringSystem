from application.common.ports.unit_of_work import UnitOfWork
from domain.company_activity.models import CompanyActivity

from ..command.create_company_activity import CreateCompanyActivityCommand


class CreateCompanyActivityHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateCompanyActivityCommand) -> CompanyActivity:
        async with self.uow:
            entity = CompanyActivity(
                code=command.code,
                title=command.title,
            )
            result = await self.uow.company_activities.add(entity)
            await self.uow.commit()
            return result

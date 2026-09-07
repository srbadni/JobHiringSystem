from application.common.ports.unit_of_work import UnitOfWork
from domain.company_activity.models import CompanyActivity

from ..command.update_company_activity import UpdateCompanyActivityCommand


class UpdateCompanyActivityHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: UpdateCompanyActivityCommand) -> CompanyActivity:
        async with self.uow:
            entity = CompanyActivity(
                id=command.company_activity_id,
            code=command.code,
            title=command.title,
            )
            result = await self.uow.company_activities.update(entity)
            await self.uow.commit()
            return result

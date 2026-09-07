from application.common.ports.unit_of_work import UnitOfWork

from ..command.delete_company_activity import DeleteCompanyActivityCommand


class DeleteCompanyActivityHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: DeleteCompanyActivityCommand) -> None:
        async with self.uow:
            await self.uow.company_activities.delete(command.company_activity_id)
            await self.uow.commit()

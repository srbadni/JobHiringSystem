from application.common.ports.unit_of_work import UnitOfWork

from ..command.delete_job_posting import DeleteJobPostingCommand


class DeleteJobPostingHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: DeleteJobPostingCommand) -> None:
        async with self.uow:
            await self.uow.job_postings.delete(command.job_posting_id, command.company_id)
            await self.uow.commit()

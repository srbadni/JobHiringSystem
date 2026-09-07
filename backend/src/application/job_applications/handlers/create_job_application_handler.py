from application.common.ports.unit_of_work import UnitOfWork
from domain.job_application.models import JobApplication

from ..command.create_job_application import CreateJobApplicationCommand


class CreateJobApplicationHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateJobApplicationCommand) -> JobApplication:
        async with self.uow:
            application = JobApplication(
                applicant_id=command.applicant_id,
                job_posting_id=command.job_posting_id,
                folder_id=command.folder_id,
            )
            result = await self.uow.job_applications.add(application)
            await self.uow.commit()
            return result

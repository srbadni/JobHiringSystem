from application.common.ports.unit_of_work import UnitOfWork
from domain.job_application.models import JobApplication
from domain.user.enums import UserType

from ..command.create_job_application import CreateJobApplicationCommand
from ...authentication.exceptions import UserNotFound
from ...common.exceptions import UserTypeError


class CreateJobApplicationHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateJobApplicationCommand) -> JobApplication:
        async with self.uow:
            user = await self.uow.users.get_by_id(command.applicant_id)
            if not user:
                raise UserNotFound
            if user.user_type == UserType.EMPLOYER:
                raise UserTypeError
            application = JobApplication.create(
                applicant_id=command.applicant_id,
                job_posting_id=command.job_posting_id,
                folder_id=command.folder_id,
            )
            result = await self.uow.job_applications.add(application)
            await self.uow.commit()
            return result

from application.common.ports.unit_of_work import UnitOfWork
from domain.job_application.models import JobApplication

from ..query.get_job_application import GetJobApplicationQuery


class GetJobApplicationHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetJobApplicationQuery) -> JobApplication:
        async with self.uow:
            return await self.uow.job_applications.get_by_id(query.application_id)

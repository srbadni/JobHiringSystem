from application.common.ports.unit_of_work import UnitOfWork
from domain.job_application.models import JobApplication

from ..query.list_my_job_applications import ListMyJobApplicationsQuery


class ListMyJobApplicationsHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: ListMyJobApplicationsQuery) -> list[JobApplication]:
        async with self.uow:
            return await self.uow.job_applications.list_by_applicant(query.applicant_id)

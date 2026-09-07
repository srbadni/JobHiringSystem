from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.job_applications.ports.job_application_repository import JobApplicationRepository
from domain.job_application.models import JobApplication
from domain.job_application.exceptions import DuplicateJobApplicationError, JobApplicationNotFoundError
from ..models.job_application import JobApplication as JobApplicationORMModel
from ..models.job_posting import JobPosting as JobPostingORMModel


class SqlAlchemyJobApplicationRepository(JobApplicationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def _to_domain(model: JobApplicationORMModel) -> JobApplication:
        return JobApplication(
            id=model.id,
            applicant_id=model.applicant_id,
            job_posting_id=model.job_posting_id,
            folder_id=model.folder_id,
            status=model.status,
        )

    async def add(self, application: JobApplication) -> JobApplication:
        job = await self.session.scalar(
            select(JobPostingORMModel.id).where(JobPostingORMModel.id == application.job_posting_id)
        )
        if job is None:
            raise JobApplicationNotFoundError(
                "Job posting was not found"
            )

        existing_application = await self.session.scalar(
            select(JobApplicationORMModel.id).where(
                JobApplicationORMModel.applicant_id == application.applicant_id,
                JobApplicationORMModel.job_posting_id == application.job_posting_id,
            )
        )
        if existing_application is not None:
            raise DuplicateJobApplicationError(
                "The applicant has already applied to this job posting"
            )

        model = JobApplicationORMModel(
            applicant_id=application.applicant_id,
            job_posting_id=application.job_posting_id,
            folder_id=application.folder_id,
            status=application.status,
        )
        self.session.add(model)
        await self.session.flush()
        return self._to_domain(model)

    async def list_by_applicant(self, applicant_id: UUID) -> list[JobApplication]:
        models = await self.session.scalars(
            select(JobApplicationORMModel).where(
                JobApplicationORMModel.applicant_id == applicant_id
            )
        )
        return [self._to_domain(model) for model in models.all()]

    async def get_by_id(self, application_id: UUID, applicant_id: UUID) -> JobApplication:
        model = await self.session.scalar(select(JobApplicationORMModel).where(
            JobApplicationORMModel.id == application_id,
            JobApplicationORMModel.applicant_id == applicant_id,
        ))
        if model is None:
            raise JobApplicationNotFoundError("Job application was not found")
        return self._to_domain(model)

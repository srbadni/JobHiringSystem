from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.job_management.ports.job_posting_respository import JobPostingRepository
from domain.job_posting.models import JobPosting
from ..models.job_posting import JobPosting as JobPostingORMModel


class SqlAlchemyJobPostingRepository(JobPostingRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def _to_domain(model: JobPostingORMModel) -> JobPosting:
        return JobPosting(
            company_id=model.company_id,
            job_category_id=model.job_category_id,
            province_id=model.province_id,
            city_id=model.city_id,
            salary_range_id=model.salary_range_id,
            job_title=model.job_title,
            job_description=model.job_description,
            company_overview=model.company_overview,
            is_latin_text=model.is_latin_text,
            post_notifications=model.post_notifications,
            employment_type=model.employment_type,
            work_mode=model.work_mode,
            status=model.status,
            work_experience=model.work_experience,
            minimum_education=model.minimum_education,
            gender=model.gender,
            military_status=model.military_status,
            id=model.id,
        )

    async def list(self, company_id: UUID) -> list[JobPosting]:
        result = await self.session.scalars(select(JobPostingORMModel).where(JobPostingORMModel.company_id == company_id))
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, job_posting_id: UUID, company_id: UUID) -> JobPosting:
        model = (await self.session.scalars(select(JobPostingORMModel).where(
            JobPostingORMModel.id == job_posting_id, JobPostingORMModel.company_id == company_id))).one()
        return self._to_domain(model)

    async def add(self, job_posting: JobPosting) -> JobPosting:
        job_posting_orm_model = JobPostingORMModel(
            id=job_posting.id,
            company_id=job_posting.company_id,
            job_category_id=job_posting.job_category_id,
            province_id=job_posting.province_id,
            city_id=job_posting.city_id,
            salary_range_id=job_posting.salary_range_id,
            job_title=job_posting.job_title,
            job_description=job_posting.job_description,
            company_overview=job_posting.company_overview,
            is_latin_text=job_posting.is_latin_text,
            post_notifications=job_posting.post_notifications,
            employment_type=job_posting.employment_type,
            work_mode=job_posting.work_mode,
            status=job_posting.status,
            work_experience=job_posting.work_experience,
            minimum_education=job_posting.minimum_education,
            gender=job_posting.gender,
            military_status=job_posting.military_status,
        )

        self.session.add(job_posting_orm_model)
        await self.session.flush()

        return self._to_domain(job_posting_orm_model)

    async def update(self, job_posting: JobPosting) -> JobPosting:
        model = await self.session.get_one(JobPostingORMModel, job_posting.id)
        model.company_id = job_posting.company_id
        model.job_category_id = job_posting.job_category_id
        model.province_id = job_posting.province_id
        model.city_id = job_posting.city_id
        model.salary_range_id = job_posting.salary_range_id
        model.job_title = job_posting.job_title
        model.job_description = job_posting.job_description
        model.company_overview = job_posting.company_overview
        model.is_latin_text = job_posting.is_latin_text
        model.post_notifications = job_posting.post_notifications
        model.employment_type = job_posting.employment_type
        model.work_mode = job_posting.work_mode
        model.status = job_posting.status
        model.work_experience = job_posting.work_experience
        model.minimum_education = job_posting.minimum_education
        model.gender = job_posting.gender
        model.military_status = job_posting.military_status
        await self.session.flush()
        return self._to_domain(model)

    async def delete(self, job_posting_id: UUID, company_id: UUID) -> None:
        model = (await self.session.scalars(select(JobPostingORMModel).where(
            JobPostingORMModel.id == job_posting_id, JobPostingORMModel.company_id == company_id))).one()
        await self.session.delete(model)
        await self.session.flush()

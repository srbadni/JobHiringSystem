from sqlalchemy.ext.asyncio import AsyncSession

from application.job_posting.ports.job_posting_respository import JobPostingRepository
from domain.job_posting.models import JobPosting
from ..models.job_posting import JobPosting as JobPostingORMModel


class SqlAlchemyJobPostingRepository(JobPostingRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, job_posting: JobPosting) -> JobPosting:
        job_posting_orm_model = JobPostingORMModel(
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

        return JobPosting(
            company_id=job_posting_orm_model.company_id,
            job_category_id=job_posting_orm_model.job_category_id,
            province_id=job_posting_orm_model.province_id,
            city_id=job_posting_orm_model.city_id,
            salary_range_id=job_posting_orm_model.salary_range_id,
            job_title=job_posting_orm_model.job_title,
            job_description=job_posting_orm_model.job_description,
            company_overview=job_posting_orm_model.company_overview,
            is_latin_text=job_posting_orm_model.is_latin_text,
            post_notifications=job_posting_orm_model.post_notifications,
            employment_type=job_posting_orm_model.employment_type,
            work_mode=job_posting_orm_model.work_mode,
            status=job_posting_orm_model.status,
            work_experience=job_posting_orm_model.work_experience,
            minimum_education=job_posting_orm_model.minimum_education,
            gender=job_posting_orm_model.gender,
            military_status=job_posting_orm_model.military_status,
            id=job_posting_orm_model.id,
        )

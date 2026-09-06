from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement

from application.jobs_search.dto.job_search_result import JobSearchResult
from application.jobs_search.ports.jobs_search_repository import (
    JobsSearchRepository,
    GetJobsQueries,
    GetCompanyJobsQueries,
)
from ..models.job_posting import JobPosting as JobPostingORMModel
from ..models.company import Company as CompanyORMModel
from ..models.job_categories import JobCategory as JobCategoryORMModel
from ..models.province import Province as ProvinceORMModel
from ..models.salary_range import SalaryRange as SalaryRangeORMModel
from ..models.city import City as CityORMModel


class SQLAlchemyJobsSearchRepository(JobsSearchRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_jobs(self, queries: GetJobsQueries) -> list[JobSearchResult]:
        filters: list[ColumnElement[bool]] = []

        if queries.keywords:
            filters.append(
                JobPostingORMModel.job_title.ilike(f"%{queries.keywords}%")
            )

        if queries.province_ids:
            filters.append(
                JobPostingORMModel.province_id.in_(queries.province_ids)
            )

        if queries.job_category_ids:
            filters.append(
                JobPostingORMModel.job_category_id.in_(queries.job_category_ids)
            )

        if queries.work_modes:
            filters.append(
                JobPostingORMModel.work_mode.in_(queries.work_modes)
            )

        if queries.work_experiences:
            filters.append(
                JobPostingORMModel.work_experience.in_(queries.work_experiences)
            )

        if queries.salary_range_ids:
            filters.append(
                JobPostingORMModel.salary_range_id.in_(queries.salary_range_ids)
            )

        stmt = (
            select(
                *JobPostingORMModel.__table__.c,
                CompanyORMModel.persian_name.label("company_title"),
                CompanyORMModel.name.label("company_english_title"),
                CompanyORMModel.logo_path.label("company_logo"),
                JobCategoryORMModel.title.label("job_category_title"),
                ProvinceORMModel.name.label("province_title"),
                SalaryRangeORMModel.title.label("salary_range_title"),
                CityORMModel.name.label("city_title"),
            )
            .join(
                CompanyORMModel,
                JobPostingORMModel.company_id == CompanyORMModel.id,
            )
            .join(
                JobCategoryORMModel,
                JobPostingORMModel.job_category_id == JobCategoryORMModel.id,
            )
            .join(
                ProvinceORMModel,
                JobPostingORMModel.province_id == ProvinceORMModel.id,
            )
            .join(
                SalaryRangeORMModel,
                JobPostingORMModel.salary_range_id == SalaryRangeORMModel.id,
            )
            .join(
                CityORMModel,
                JobPostingORMModel.city_id == CityORMModel.id,
            )
            .where(*filters)
        )

        result = await self.session.execute(stmt)
        rows = result.mappings().all()

        return [
            JobSearchResult(
                id=row.id,
                company_id=row.company_id,
                company_title=row.company_title,
                company_english_title=row.company_english_title,
                company_logo=row.company_logo,
                job_category_title=row.job_category_title,
                province_title=row.province_title,
                city_title=row.city_title,
                salary_range_title=row.salary_range_title,
                job_title=row.job_title,
            )
            for row in rows
        ]

    async def get_company_jobs(
        self,
        queries: GetCompanyJobsQueries,
    ) -> list[JobSearchResult]:

        stmt = (
            select(
                *JobPostingORMModel.__table__.c,
                CompanyORMModel.persian_name.label("company_title"),
                CompanyORMModel.name.label("company_english_title"),
                CompanyORMModel.logo_path.label("company_logo"),
                JobCategoryORMModel.title.label("job_category_title"),
                ProvinceORMModel.name.label("province_title"),
                SalaryRangeORMModel.title.label("salary_range_title"),
                CityORMModel.name.label("city_title"),
            )
            .join(
                CompanyORMModel,
                JobPostingORMModel.company_id == CompanyORMModel.id,
            )
            .join(
                JobCategoryORMModel,
                JobPostingORMModel.job_category_id == JobCategoryORMModel.id,
            )
            .join(
                ProvinceORMModel,
                JobPostingORMModel.province_id == ProvinceORMModel.id,
            )
            .join(
                SalaryRangeORMModel,
                JobPostingORMModel.salary_range_id == SalaryRangeORMModel.id,
            )
            .join(
                CityORMModel,
                JobPostingORMModel.city_id == CityORMModel.id,
            )
            .where(
                CompanyORMModel.name == queries.company_en_name
            )
        )

        result = await self.session.execute(stmt)
        rows = result.mappings().all()

        return [
            JobSearchResult(
                id=row.id,
                company_id=row.company_id,
                company_title=row.company_title,
                company_english_title=row.company_english_title,
                company_logo=row.company_logo,
                job_category_title=row.job_category_title,
                province_title=row.province_title,
                city_title=row.city_title,
                salary_range_title=row.salary_range_title,
                job_title=row.job_title,
            )
            for row in rows
        ]
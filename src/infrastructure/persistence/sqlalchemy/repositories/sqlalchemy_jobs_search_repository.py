from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement

from application.jobs_search.dto.job_details import JobDetails
from application.jobs_search.dto.company_details import CompanyDetails
from application.jobs_search.dto.job_search_result import JobSearchResult
from application.jobs_search.ports.jobs_search_repository import (
    JobsSearchRepository,
    GetJobsQueries,
    GetCompanyJobsQueries, GetCompanyDetailsQueries, GetJobDetailsQueries,
)
from ..models.job_posting import JobPosting as JobPostingORMModel
from ..models.company import Company as CompanyORMModel
from ..models.job_categories import JobCategory as JobCategoryORMModel
from ..models.company_activity import CompanyActivity as CompanyActivityORMModel
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

    async def get_job_details(self, queries: GetJobDetailsQueries) -> JobDetails:
        stmt = (select(
            *JobPostingORMModel.__table__.c,
            CompanyORMModel.persian_name.label("company_title"),
            CompanyORMModel.name.label("company_en_title"),
            CompanyORMModel.personnel_count.label("company_employee_count"),
            CompanyActivityORMModel.title.label("company_activity"),
            CityORMModel.name.label("city"),
            ProvinceORMModel.name.label("province"),
            JobCategoryORMModel.title.label("job_category"),
            SalaryRangeORMModel.title.label("salary_range"),
        )
        .join(JobPostingORMModel.company)
        .join(CompanyORMModel.activity)
        .join(JobPostingORMModel.city)
        .join(JobPostingORMModel.province)
        .join(JobPostingORMModel.job_category)
        .join(JobPostingORMModel.salary_range)
        .where(
            JobPostingORMModel.id == queries.job_posting_id,
            CompanyORMModel.name == queries.company_en_name,
        )
        )

        result = await self.session.execute(stmt)
        details = result.mappings().one_or_none()

        if details is None:
            raise Exception

        return JobDetails(
            id=details.id,
            company_title=details.company_title,
            company_en_title=details.company_en_title,
            company_activity=details.company_activity,
            company_employee_count=details.company_employee_count,
            city=details.city,
            province=details.province,
            job_category=details.job_category,
            job_title=details.job_title,
            job_description=details.job_description,
            company_overview=details.company_overview,
            employment_type=details.employment_type,
            work_mode=details.work_mode,
            salary_range=details.salary_range,
            work_experience=details.work_experience,
            minimum_education=details.minimum_education,
            gender=details.gender,
            military_status=details.military_status,
            post_notifications=details.post_notifications,
            status=details.status,
        )

    async def get_company_details(self, queries: GetCompanyDetailsQueries) -> CompanyDetails:
        stmt = (
            select(
                CompanyORMModel.persian_name.label("name"),
                CompanyORMModel.name.label("english_name"),
                CompanyActivityORMModel.title.label("activity"),
                CompanyORMModel.personnel_count.label("employee_count"),
                CityORMModel.name.label("city"),
                ProvinceORMModel.name.label("province"),
            )
            .join(CompanyORMModel.activity)
            .join(CompanyORMModel.city)
            .join(CompanyORMModel.province)
            .where(CompanyORMModel.name == queries.company_en_name)
        )

        result = await self.session.execute(stmt)
        details = result.mappings().one_or_none()

        if details is None:
            raise Exception

        return CompanyDetails(
            name=details.name,
            english_name=details.english_name,
            activity=details.activity,
            employee_count=details.employee_count,
            city=details.city,
            province=details.province,
        )

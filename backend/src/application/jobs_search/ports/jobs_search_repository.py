from uuid import UUID
from abc import ABC, abstractmethod
from dataclasses import dataclass

from application.common.dto.pagination import PaginatedResult
from application.jobs_search.dto.job_details import JobDetails
from application.jobs_search.dto.company_details import CompanyDetails
from application.jobs_search.dto.job_search_result import SearchJob
from application.jobs_search.query.get_jobs import SortType
from domain.job_posting.enum import WorkMode, RelevantWorkExperience


@dataclass(slots=True)
class GetJobsQueries:
    page_size: int
    page_index: int
    sort_type: SortType | None
    keywords: str | None = None
    province_ids: list[UUID] | None = None
    job_category_ids: list[UUID] | None = None
    work_modes: list[WorkMode] | None = None
    work_experiences: list[RelevantWorkExperience] | None = None
    salary_range_ids: list[UUID] | None = None

@dataclass(slots=True)
class GetCompanyJobsQueries:
    company_en_name: str

@dataclass(slots=True)
class GetCompanyDetailsQueries:
    company_en_name: str

@dataclass(slots=True)
class GetJobDetailsQueries:
    job_posting_id: UUID
    company_en_name: str


class JobsSearchRepository(ABC):

    @abstractmethod
    async def get_jobs(self, queries: GetJobsQueries) -> PaginatedResult[SearchJob]:
        pass

    @abstractmethod
    async def get_company_jobs(self, queries: GetCompanyJobsQueries) -> list[SearchJob]:
        pass

    @abstractmethod
    async def get_company_details(self, queries: GetCompanyDetailsQueries) -> CompanyDetails:
        pass

    @abstractmethod
    async def get_job_details(self, queries: GetJobDetailsQueries) -> JobDetails:
        pass

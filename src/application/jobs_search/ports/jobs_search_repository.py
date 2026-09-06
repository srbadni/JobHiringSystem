from uuid import UUID
from abc import ABC, abstractmethod
from dataclasses import dataclass

from application.jobs_search.dto.job_details import JobDetails
from application.jobs_search.dto.job_search_result import JobSearchResult
from domain.job_posting.enum import WorkMode, RelevantWorkExperience


@dataclass(slots=True)
class GetJobsQueries:
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
class GetJobDetailsQueries:
    job_posting_id: UUID
    company_en_name: str


class JobsSearchRepository(ABC):

    @abstractmethod
    async def get_jobs(self, queries: GetJobsQueries) -> list[JobSearchResult]:
        pass

    @abstractmethod
    async def get_company_jobs(self, queries: GetCompanyJobsQueries) -> list[JobSearchResult]:
        pass

    @abstractmethod
    async def get_job_details(self, queries: GetJobDetailsQueries) -> JobDetails:
        pass

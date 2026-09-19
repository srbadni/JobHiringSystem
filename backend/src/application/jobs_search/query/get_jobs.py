from enum import StrEnum
from uuid import UUID
from dataclasses import dataclass

from domain.job_posting.enum import WorkMode, RelevantWorkExperience

class SortType(StrEnum):
    RELEVANCE = "relevance"
    MOST_RECENT = "most_recent"
    SALARY_DESC = "salary_desc"

@dataclass(frozen=True)
class GetJobsQuery:
    page_size: int
    page_index: int
    sort_type: SortType | None
    keywords: str | None = None
    province_ids: list[UUID] | None = None
    job_category_ids: list[UUID] | None = None
    work_modes: list[WorkMode] | None = None
    work_experiences: list[RelevantWorkExperience] | None = None
    salary_range_ids: list[UUID] | None = None

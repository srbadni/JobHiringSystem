from uuid import UUID
from dataclasses import dataclass

from domain.job_posting.enum import WorkMode, RelevantWorkExperience


@dataclass(frozen=True)
class GetJobsQuery:
    keywords: str | None = None
    province_ids: list[UUID] | None = None
    job_category_ids: list[UUID] | None = None
    work_modes: list[WorkMode] | None = None
    work_experiences: list[RelevantWorkExperience] | None = None
    salary_range_ids: list[UUID] | None = None
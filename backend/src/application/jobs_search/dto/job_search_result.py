from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from uuid import UUID

from ...common.dto.pagination import Pagination
from domain.job_posting.enum import EmploymentType, WorkMode

@dataclass(frozen=True)
class JobResults:
    jobs: list[SearchJob]
    pagination: Pagination
    facets: Dict | None = None


@dataclass(frozen=True)
class SearchJob:
    id: UUID
    company_id: UUID
    company_title: str
    company_english_title: str
    company_logo: str | None

    job_category_title: str

    province_title: str

    city_title: str

    salary_title: str
    employment_type: EmploymentType
    work_mode: WorkMode

    job_title: str
    created_at: datetime

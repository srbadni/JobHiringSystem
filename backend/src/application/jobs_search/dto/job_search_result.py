from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from domain.job_posting.enum import EmploymentType, WorkMode


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

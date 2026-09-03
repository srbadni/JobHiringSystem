from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class JobSearchResult:
    id: int
    company_id: UUID
    company_title: str
    company_english_title: str
    company_logo: str | None

    job_category_title: str

    province_title: str

    city_title: str

    salary_range_title: str

    job_title: str
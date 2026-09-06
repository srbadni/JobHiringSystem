from dataclasses import dataclass
from uuid import UUID

from domain.job_posting.enum import EmploymentType, WorkMode, JobPostingStatus, RelevantWorkExperience, \
    MinimumEducationLevel, Gender, MilitaryServiceStatus

@dataclass(frozen=True)
class CreateJobPostingCommand:
    company_id: UUID
    job_category_id: UUID
    province_id: UUID
    city_id: UUID
    salary_range_id: UUID
    job_title: str
    job_description: str
    company_overview: str
    is_latin_text: bool
    employment_type: EmploymentType
    work_mode: WorkMode
    status: JobPostingStatus
    work_experience: RelevantWorkExperience
    minimum_education: MinimumEducationLevel
    gender: Gender
    military_status: MilitaryServiceStatus

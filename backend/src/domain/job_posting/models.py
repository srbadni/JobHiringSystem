from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .enum import EmploymentType, WorkMode, JobPostingStatus, RelevantWorkExperience, Gender, MinimumEducationLevel, \
    MilitaryServiceStatus


@dataclass
class JobPosting:
    company_id: UUID
    job_category_id: UUID
    province_id: UUID
    city_id: UUID
    salary_range_id: UUID
    job_title: str
    job_description: str
    company_overview: str
    is_latin_text: bool
    post_notifications: bool
    employment_type: EmploymentType
    work_mode: WorkMode
    status: JobPostingStatus
    work_experience: RelevantWorkExperience
    minimum_education: MinimumEducationLevel
    gender: Gender
    military_status: MilitaryServiceStatus
    id: UUID = field(default_factory=uuid4)

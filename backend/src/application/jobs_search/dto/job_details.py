from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.company.enums import EmployeeCount
from domain.job_posting.enum import EmploymentType, WorkMode, RelevantWorkExperience, MinimumEducationLevel, Gender, \
    MilitaryServiceStatus, JobPostingStatus


@dataclass
class JobDetails:
    id: UUID
    company_title: str
    company_en_title: str
    company_activity: str
    company_employee_count: EmployeeCount
    city: str
    province: str
    job_category: str
    job_title: str
    job_description: str
    company_overview: str
    employment_type: EmploymentType
    work_mode: WorkMode
    salary_range: str
    work_experience: RelevantWorkExperience
    minimum_education: MinimumEducationLevel
    gender: Gender
    military_status: MilitaryServiceStatus
    post_notifications: bool
    status: JobPostingStatus
    created_at: datetime

from uuid import UUID
from pydantic import BaseModel

from domain.job_posting.enum import Gender, MilitaryServiceStatus, MinimumEducationLevel, RelevantWorkExperience, \
    WorkMode, EmploymentType

class JobSearchRead(BaseModel):
    id: UUID
    job_title: str
    employment_type: EmploymentType
    work_mode: WorkMode
    work_experience: RelevantWorkExperience
    minimum_education: MinimumEducationLevel
    gender: Gender
    military_status: MilitaryServiceStatus
    post_notifications: bool
    company_title: str
    company_english_title: str
    company_logo: str | None
    job_category_title: str
    province_title: str
    salary_range_title: str
    city_title: str
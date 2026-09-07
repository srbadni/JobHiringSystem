from uuid import UUID
from pydantic import BaseModel

from domain.job_posting.enum import Gender, MilitaryServiceStatus, MinimumEducationLevel, RelevantWorkExperience, \
    WorkMode, EmploymentType
from domain.job_application.enums import ApplicationStatus


class JobApplicationCreate(BaseModel):
    applicant_id: UUID
    folder_id: UUID | None = None


class JobApplicationRead(BaseModel):
    id: UUID
    applicant_id: UUID
    job_posting_id: UUID
    folder_id: UUID | None
    status: ApplicationStatus

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

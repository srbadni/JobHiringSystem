from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from domain.company.enums import EmployeeCount
from domain.job_application.enums import ApplicationStatus
from domain.job_posting.enum import EmploymentType, Gender, JobPostingStatus, MilitaryServiceStatus, MinimumEducationLevel, RelevantWorkExperience, WorkMode

class JobSearchRead(BaseModel):
    id: UUID
    company_id: UUID
    company_title: str
    company_english_title: str
    company_logo: str | None
    job_category_title: str
    province_title: str
    city_title: str
    salary_range_title: str
    job_title: str

class CompanyRead(BaseModel):
    name: str
    english_name: str
    activity: str
    employee_count: EmployeeCount
    city: str
    province: str

class JobDetailsRead(BaseModel):
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

class JobApplicationCreate(BaseModel):
    folder_id: UUID | None = None

class JobApplicationRead(BaseModel):
    id: UUID
    applicant_id: UUID
    job_posting_id: UUID
    folder_id: UUID | None
    status: ApplicationStatus

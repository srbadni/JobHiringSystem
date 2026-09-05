from uuid import UUID

from pydantic import BaseModel, Field

from domain.job_posting.enum import EmploymentType, WorkMode, JobPostingStatus, RelevantWorkExperience, \
    MinimumEducationLevel, Gender, MilitaryServiceStatus


class JobPostingCreate(BaseModel):
    company_id: UUID
    job_category_id: int
    province_id: int
    city_id: int
    salary_range_id: int
    job_title: str = Field(min_length=5)
    job_description: str = Field(min_length=40)
    company_overview: str = Field(min_length=40)
    is_latin_text: bool
    employment_type: EmploymentType
    work_mode: WorkMode
    status: JobPostingStatus
    work_experience: RelevantWorkExperience
    minimum_education: MinimumEducationLevel
    gender: Gender
    military_status: MilitaryServiceStatus

class JobPostingRead(BaseModel):
    id: UUID
    company_id: UUID
    job_category_id: int
    province_id: int
    city_id: int
    salary_range_id: int
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


class JobPostingUpdate(JobPostingCreate):
    pass

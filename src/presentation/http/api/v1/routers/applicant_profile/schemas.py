from uuid import UUID

from pydantic import BaseModel, Field, model_validator

from domain.applicant_education_history.enums import EducationLevel
from domain.applicant_language.enums import LanguageLevel
from domain.job_preference.enums import PreferredEmploymentType, PreferredJobBenefit, PreferredSeniorityLevel


def _uuid_list() -> list[UUID]:
    return []


def _employment_type_list() -> list[PreferredEmploymentType]:
    return []


def _seniority_list() -> list[PreferredSeniorityLevel]:
    return []


def _benefit_list() -> list[PreferredJobBenefit]:
    return []


class SkillInput(BaseModel):
    title: str = Field(min_length=1, max_length=90)


class SkillRead(SkillInput):
    id: UUID


class WorkExperienceInput(BaseModel):
    position_title: str = Field(min_length=1, max_length=200)
    workplace_name: str = Field(min_length=1)
    start_month: int = Field(ge=1, le=12)
    start_year: int = Field(ge=1900, le=2200)
    end_month: int | None = Field(default=None, ge=1, le=12)
    end_year: int | None = Field(default=None, ge=1900, le=2200)
    is_current: bool | None = None
    experience_description: str | None = None

    @model_validator(mode="after")
    def validate_end_date(self) -> "WorkExperienceInput":
        if self.is_current is True and (self.end_month is not None or self.end_year is not None):
            raise ValueError("A current position cannot have an end date")
        if self.is_current is False and (self.end_month is None or self.end_year is None):
            raise ValueError("A previous position must have a complete end date")
        return self


class WorkExperienceRead(WorkExperienceInput):
    id: UUID


class EducationInput(BaseModel):
    institution_name: str = Field(min_length=1, max_length=200)
    field_of_study: str = Field(min_length=1, max_length=200)
    education_level: EducationLevel
    start_year: int = Field(ge=1900, le=2200)
    end_year: int | None = Field(default=None, ge=1900, le=2200)
    is_currently_studying: bool = False
    description: str | None = None

    @model_validator(mode="after")
    def validate_end_year(self) -> "EducationInput":
        if self.is_currently_studying == (self.end_year is not None):
            raise ValueError("Current education must not have an end year; completed education must have one")
        return self


class EducationRead(EducationInput):
    id: UUID


class LanguageSkillInput(BaseModel):
    language_name: str = Field(min_length=1, max_length=100)
    level: LanguageLevel


class LanguageSkillRead(LanguageSkillInput):
    id: UUID


class JobPreferenceInput(BaseModel):
    minimum_salary_range_id: UUID | None = None
    job_category_ids: list[UUID] = Field(default_factory=_uuid_list)
    province_ids: list[UUID] = Field(default_factory=_uuid_list)
    employment_types: list[PreferredEmploymentType] = Field(default_factory=_employment_type_list)
    seniority_levels: list[PreferredSeniorityLevel] = Field(default_factory=_seniority_list)
    benefits: list[PreferredJobBenefit] = Field(default_factory=_benefit_list)


class JobPreferenceRead(JobPreferenceInput):
    id: UUID

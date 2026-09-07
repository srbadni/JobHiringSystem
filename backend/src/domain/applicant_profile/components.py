from dataclasses import dataclass, field
from uuid import UUID, uuid4

from domain.applicant_education_history.enums import EducationLevel
from domain.applicant_language.enums import LanguageLevel
from domain.job_preference.enums import (
    PreferredEmploymentType,
    PreferredJobBenefit,
    PreferredSeniorityLevel,
)


def _uuid_list() -> list[UUID]:
    return []


def _employment_type_list() -> list[PreferredEmploymentType]:
    return []


def _seniority_list() -> list[PreferredSeniorityLevel]:
    return []


def _benefit_list() -> list[PreferredJobBenefit]:
    return []


@dataclass(slots=True)
class ApplicantSkill:
    title: str
    id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class WorkExperience:
    position_title: str
    workplace_name: str
    start_month: int
    start_year: int
    end_month: int | None = None
    end_year: int | None = None
    is_current: bool | None = None
    experience_description: str | None = None
    id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class Education:
    institution_name: str
    field_of_study: str
    education_level: EducationLevel
    start_year: int
    end_year: int | None = None
    is_currently_studying: bool = False
    description: str | None = None
    id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class LanguageSkill:
    language_name: str
    level: LanguageLevel
    id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class JobPreference:
    minimum_salary_range_id: UUID | None = None
    job_category_ids: list[UUID] = field(default_factory=_uuid_list)
    province_ids: list[UUID] = field(default_factory=_uuid_list)
    employment_types: list[PreferredEmploymentType] = field(default_factory=_employment_type_list)
    seniority_levels: list[PreferredSeniorityLevel] = field(default_factory=_seniority_list)
    benefits: list[PreferredJobBenefit] = field(default_factory=_benefit_list)
    id: UUID = field(default_factory=uuid4)

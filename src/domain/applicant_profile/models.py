from dataclasses import dataclass, field
from uuid import UUID, uuid4

from ..applicant_profile.enum import Gender, MartialStatus
from ..attached_resume.models import AttachedResume
from ..job_posting.enum import MilitaryServiceStatus
from .components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience


def _skills() -> list[ApplicantSkill]:
    return []


def _work_experiences() -> list[WorkExperience]:
    return []


def _educations() -> list[Education]:
    return []


def _language_skills() -> list[LanguageSkill]:
    return []

@dataclass
class ApplicantProfile:
    applicant_id: UUID
    specialization: str | None = None
    birth_year: int | None = None
    gender: Gender | None = None
    military_status: MilitaryServiceStatus | None = None
    martial_status: MartialStatus | None = None
    province: str | None = None
    address: str | None = None
    about: str | None = None
    attached_resume: AttachedResume | None = None
    skills: list[ApplicantSkill] = field(default_factory=_skills)
    work_experiences: list[WorkExperience] = field(default_factory=_work_experiences)
    educations: list[Education] = field(default_factory=_educations)
    language_skills: list[LanguageSkill] = field(default_factory=_language_skills)
    job_preference: JobPreference | None = None
    id: UUID = field(default_factory=uuid4)

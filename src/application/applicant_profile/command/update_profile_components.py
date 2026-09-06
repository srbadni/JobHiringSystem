from dataclasses import dataclass
from uuid import UUID

from domain.applicant_profile.components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience


@dataclass(frozen=True, slots=True)
class ReplaceSkillsCommand:
    applicant_id: UUID
    items: list[ApplicantSkill]


@dataclass(frozen=True, slots=True)
class ReplaceWorkExperiencesCommand:
    applicant_id: UUID
    items: list[WorkExperience]


@dataclass(frozen=True, slots=True)
class ReplaceEducationsCommand:
    applicant_id: UUID
    items: list[Education]


@dataclass(frozen=True, slots=True)
class ReplaceLanguageSkillsCommand:
    applicant_id: UUID
    items: list[LanguageSkill]


@dataclass(frozen=True, slots=True)
class ReplaceJobPreferenceCommand:
    applicant_id: UUID
    item: JobPreference

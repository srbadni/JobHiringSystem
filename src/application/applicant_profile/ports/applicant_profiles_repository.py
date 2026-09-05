from abc import ABC, abstractmethod
from uuid import UUID

from domain.applicant_profile.models import ApplicantProfile
from domain.applicant_profile.components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience


class ApplicantProfilesRepository(ABC):

    @abstractmethod
    async def add(self, applicant_profile: ApplicantProfile) -> ApplicantProfile:
        pass

    @abstractmethod
    async def replace_skills(self, applicant_id: UUID, items: list[ApplicantSkill]) -> list[ApplicantSkill]: ...

    @abstractmethod
    async def replace_work_experiences(self, applicant_id: UUID, items: list[WorkExperience]) -> list[WorkExperience]: ...

    @abstractmethod
    async def replace_educations(self, applicant_id: UUID, items: list[Education]) -> list[Education]: ...

    @abstractmethod
    async def replace_language_skills(self, applicant_id: UUID, items: list[LanguageSkill]) -> list[LanguageSkill]: ...

    @abstractmethod
    async def replace_job_preference(self, applicant_id: UUID, item: JobPreference) -> JobPreference: ...

from abc import ABC, abstractmethod

from domain.applicant_profile.models import ApplicantProfile


class ApplicantProfilesRepository(ABC):

    @abstractmethod
    async def add(self, applicant_profile: ApplicantProfile) -> ApplicantProfile:
        pass
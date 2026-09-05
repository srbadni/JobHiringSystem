from abc import ABC, abstractmethod
from domain.attached_resume.models import AttachedResume


class AttachedResumesRepository(ABC):

    @abstractmethod
    async def add(self, attached_resume: AttachedResume) -> AttachedResume:
        pass
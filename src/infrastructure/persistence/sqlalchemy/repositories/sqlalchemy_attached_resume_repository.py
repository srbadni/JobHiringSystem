from sqlalchemy.ext.asyncio import AsyncSession

from application.attached_resume.ports.attached_resumes_repository import AttachedResumesRepository
from domain.attached_resume.models import AttachedResume
from ..models.attached_resume import AttachedResume as AttachedResumeORMModel


class SQLAlchemyAttachedResumesRepository(AttachedResumesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, attached_resume: AttachedResume) -> AttachedResume:
        model = AttachedResumeORMModel(
            media_id=attached_resume.media_id,
            applicant_profile_id=attached_resume.applicant_profile_id,
        )
        self.session.add(model)
        await self.session.flush()
        return AttachedResume(
            media_id=model.media_id,
            applicant_profile_id=model.applicant_profile_id,
            id=model.id,
        )

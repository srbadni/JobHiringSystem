from sqlalchemy.ext.asyncio import AsyncSession

from application.applicant_profile.ports.applicant_profiles_repository import ApplicantProfilesRepository
from domain.applicant_profile.models import ApplicantProfile
from domain.attached_resume.models import AttachedResume
from ..models.applicant_profile import ApplicantProfile as ApplicantProfileORMModel


class SQLAlchemyApplicantProfilesRepository(ApplicantProfilesRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, applicant_profile: ApplicantProfile) -> ApplicantProfile:
        applicant_profile_orm_model = ApplicantProfileORMModel(
            id=applicant_profile.id,
            applicant_id=applicant_profile.applicant_id,
            specialization=applicant_profile.specialization,
            birth_year=applicant_profile.birth_year,
            gender=applicant_profile.gender,
            military_status=applicant_profile.military_status,
            martial_status=applicant_profile.martial_status,
            province=applicant_profile.province,
            address=applicant_profile.address,
            about=applicant_profile.about,
        )
        self.session.add(applicant_profile_orm_model)

        mapped_attached_resume = None

        if applicant_profile_orm_model.attached_resume:
            mapped_attached_resume = AttachedResume(
                media_id=applicant_profile_orm_model.attached_resume.media_id,
                applicant_profile_id=applicant_profile_orm_model.attached_resume.applicant_profile_id,
                id=applicant_profile_orm_model.attached_resume.id,
            )

        return ApplicantProfile(
            applicant_id=applicant_profile_orm_model.applicant_id,
            specialization=applicant_profile_orm_model.specialization,
            birth_year=applicant_profile_orm_model.birth_year,
            gender=applicant_profile_orm_model.gender,
            military_status=applicant_profile_orm_model.military_status,
            martial_status=applicant_profile_orm_model.martial_status,
            province=applicant_profile_orm_model.province,
            address=applicant_profile_orm_model.address,
            about=applicant_profile_orm_model.about,
            attached_resume=mapped_attached_resume if mapped_attached_resume else None,
            id=applicant_profile_orm_model.id,
        )

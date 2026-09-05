from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from application.applicant_profile.ports.applicant_profiles_repository import ApplicantProfilesRepository
from domain.applicant_profile.models import ApplicantProfile
from domain.attached_resume.models import AttachedResume
from domain.applicant_profile.components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience
from ..models.applicant_profile import ApplicantProfile as ApplicantProfileORMModel
from ..models.applicant_skill import ApplicantSkill as ApplicantSkillORM
from ..models.applicant_work_experience import WorkExperience as WorkExperienceORM
from ..models.applicant_education_history import Education as EducationORM
from ..models.applicant_language import LanguageSkill as LanguageSkillORM
from ..models.job_categories import JobCategory
from ..models.province import Province
from ..models.job_preference import (
    JobPreference as JobPreferenceORM,
    JobPreferenceBenefit,
    JobPreferenceEmploymentType,
    JobPreferenceSeniorityLevel,
)


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

    async def _profile_id(self, applicant_id: UUID) -> UUID:
        profile_id = await self.session.scalar(
            select(ApplicantProfileORMModel.id).where(ApplicantProfileORMModel.applicant_id == applicant_id)
        )
        if profile_id is None:
            raise LookupError("Applicant profile was not found.")
        return profile_id

    async def replace_skills(self, applicant_id: UUID, items: list[ApplicantSkill]) -> list[ApplicantSkill]:
        profile_id = await self._profile_id(applicant_id)
        await self.session.execute(delete(ApplicantSkillORM).where(ApplicantSkillORM.applicant_profile_id == profile_id))
        models = [ApplicantSkillORM(applicant_profile_id=profile_id, title=item.title) for item in items]
        for model, item in zip(models, items, strict=True): model.id = item.id
        self.session.add_all(models)
        return items

    async def replace_work_experiences(self, applicant_id: UUID, items: list[WorkExperience]) -> list[WorkExperience]:
        profile_id = await self._profile_id(applicant_id)
        await self.session.execute(delete(WorkExperienceORM).where(WorkExperienceORM.profile_id == profile_id))
        models = [WorkExperienceORM(
            profile_id=profile_id, position_title=item.position_title,
            workplace_name=item.workplace_name, start_month=item.start_month,
            start_year=item.start_year, end_month=item.end_month, end_year=item.end_year,
            is_current=item.is_current, experience_description=item.experience_description,
        ) for item in items]
        for model, item in zip(models, items, strict=True): model.id = item.id
        self.session.add_all(models)
        return items

    async def replace_educations(self, applicant_id: UUID, items: list[Education]) -> list[Education]:
        profile_id = await self._profile_id(applicant_id)
        await self.session.execute(delete(EducationORM).where(EducationORM.profile_id == profile_id))
        models: list[EducationORM] = []
        for item in items:
            model = EducationORM(
                profile_id=profile_id, institution_name=item.institution_name,
                field_of_study=item.field_of_study, education_level=item.education_level,
                start_year=item.start_year, end_year=item.end_year, description=item.description,
            )
            model.id = item.id
            model.is_currently_studying = item.is_currently_studying
            models.append(model)
        self.session.add_all(models)
        return items

    async def replace_language_skills(self, applicant_id: UUID, items: list[LanguageSkill]) -> list[LanguageSkill]:
        profile_id = await self._profile_id(applicant_id)
        await self.session.execute(delete(LanguageSkillORM).where(LanguageSkillORM.profile_id == profile_id))
        models = [LanguageSkillORM(profile_id=profile_id, language_name=item.language_name, level=item.level) for item in items]
        for model, item in zip(models, items, strict=True): model.id = item.id
        self.session.add_all(models)
        return items

    async def replace_job_preference(self, applicant_id: UUID, item: JobPreference) -> JobPreference:
        profile_id = await self._profile_id(applicant_id)
        existing_id = await self.session.scalar(
            select(JobPreferenceORM.id).where(JobPreferenceORM.profile_id == profile_id)
        )
        if existing_id is not None:
            await self.session.execute(delete(JobPreferenceORM).where(JobPreferenceORM.id == existing_id))
            await self.session.flush()

        model = JobPreferenceORM(
            profile_id=profile_id,
            minimum_salary_range_id=item.minimum_salary_range_id,
        )
        model.id = item.id
        if item.job_category_ids:
            model.job_categories = list((await self.session.scalars(
                select(JobCategory).where(JobCategory.id.in_(item.job_category_ids))
            )).all())
            if len(model.job_categories) != len(set(item.job_category_ids)):
                raise LookupError("One or more job categories were not found.")
        if item.province_ids:
            model.provinces = list((await self.session.scalars(
                select(Province).where(Province.id.in_(item.province_ids))
            )).all())
            if len(model.provinces) != len(set(item.province_ids)):
                raise LookupError("One or more provinces were not found.")
        model.employment_types = [JobPreferenceEmploymentType(
            job_preference_id=item.id, employment_type=value,
        ) for value in item.employment_types]
        model.seniority_levels = [JobPreferenceSeniorityLevel(
            job_preference_id=item.id, seniority_level=value,
        ) for value in item.seniority_levels]
        model.benefits = [JobPreferenceBenefit(
            job_preference_id=item.id, benefit=value,
        ) for value in item.benefits]
        self.session.add(model)
        return item

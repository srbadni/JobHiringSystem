from collections.abc import Callable
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from application.applicant_profile.command.update_profile_components import (
    ReplaceEducationsCommand, ReplaceJobPreferenceCommand, ReplaceLanguageSkillsCommand,
    ReplaceSkillsCommand, ReplaceWorkExperiencesCommand,
)
from application.applicant_profile.handlers.update_profile_components import (
    ReplaceEducationsHandler, ReplaceJobPreferenceHandler, ReplaceLanguageSkillsHandler,
    ReplaceSkillsHandler, ReplaceWorkExperiencesHandler,
)
from domain.applicant_profile.components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience
from .schemas import (
    EducationInput, EducationRead, JobPreferenceInput, JobPreferenceRead,
    LanguageSkillInput, LanguageSkillRead, SkillInput, SkillRead,
    WorkExperienceInput, WorkExperienceRead,
)


def create_applicant_profile_router(
    provide_skills_handler: Callable[[], ReplaceSkillsHandler],
    provide_work_experiences_handler: Callable[[], ReplaceWorkExperiencesHandler],
    provide_educations_handler: Callable[[], ReplaceEducationsHandler],
    provide_language_skills_handler: Callable[[], ReplaceLanguageSkillsHandler],
    provide_job_preference_handler: Callable[[], ReplaceJobPreferenceHandler],
) -> APIRouter:
    router = APIRouter(tags=["Applicant Profile"])

    @router.put("/{applicant_id}/skills", response_model=list[SkillRead])
    async def replace_skills(applicant_id: UUID, data: list[SkillInput], handler: Annotated[ReplaceSkillsHandler, Depends(provide_skills_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ReplaceSkillsCommand(applicant_id, [ApplicantSkill(**item.model_dump()) for item in data]))

    @router.put("/{applicant_id}/work-experiences", response_model=list[WorkExperienceRead])
    async def replace_work_experiences(applicant_id: UUID, data: list[WorkExperienceInput], handler: Annotated[ReplaceWorkExperiencesHandler, Depends(provide_work_experiences_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ReplaceWorkExperiencesCommand(applicant_id, [WorkExperience(**item.model_dump()) for item in data]))

    @router.put("/{applicant_id}/educations", response_model=list[EducationRead])
    async def replace_educations(applicant_id: UUID, data: list[EducationInput], handler: Annotated[ReplaceEducationsHandler, Depends(provide_educations_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ReplaceEducationsCommand(applicant_id, [Education(**item.model_dump()) for item in data]))

    @router.put("/{applicant_id}/language-skills", response_model=list[LanguageSkillRead])
    async def replace_language_skills(applicant_id: UUID, data: list[LanguageSkillInput], handler: Annotated[ReplaceLanguageSkillsHandler, Depends(provide_language_skills_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ReplaceLanguageSkillsCommand(applicant_id, [LanguageSkill(**item.model_dump()) for item in data]))

    @router.put("/{applicant_id}/job-preference", response_model=JobPreferenceRead)
    async def replace_job_preference(applicant_id: UUID, data: JobPreferenceInput, handler: Annotated[ReplaceJobPreferenceHandler, Depends(provide_job_preference_handler)]):  # pyright: ignore[reportUnusedFunction]
        return await handler.handle(ReplaceJobPreferenceCommand(applicant_id, JobPreference(**data.model_dump())))

    return router

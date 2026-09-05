from collections.abc import Awaitable, Callable
from typing import Generic, TypeVar

from fastapi import HTTPException, status

from application.common.ports.unit_of_work import UnitOfWork
from domain.applicant_profile.components import ApplicantSkill, Education, JobPreference, LanguageSkill, WorkExperience
from ..command.update_profile_components import (
    ReplaceEducationsCommand,
    ReplaceJobPreferenceCommand,
    ReplaceLanguageSkillsCommand,
    ReplaceSkillsCommand,
    ReplaceWorkExperiencesCommand,
)

T = TypeVar("T")
CommandT = TypeVar("CommandT")


class _BaseHandler(Generic[CommandT, T]):
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def _execute(self, operation: Callable[[CommandT], Awaitable[T]], command: CommandT) -> T:
        async with self.uow:
            try:
                result = await operation(command)
            except LookupError as exc:
                raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
            await self.uow.commit()
            return result


class ReplaceSkillsHandler(_BaseHandler[ReplaceSkillsCommand, list[ApplicantSkill]]):
    async def handle(self, command: ReplaceSkillsCommand) -> list[ApplicantSkill]:
        return await self._execute(lambda value: self.uow.applicant_profiles.replace_skills(value.applicant_id, value.items), command)


class ReplaceWorkExperiencesHandler(_BaseHandler[ReplaceWorkExperiencesCommand, list[WorkExperience]]):
    async def handle(self, command: ReplaceWorkExperiencesCommand) -> list[WorkExperience]:
        return await self._execute(lambda value: self.uow.applicant_profiles.replace_work_experiences(value.applicant_id, value.items), command)


class ReplaceEducationsHandler(_BaseHandler[ReplaceEducationsCommand, list[Education]]):
    async def handle(self, command: ReplaceEducationsCommand) -> list[Education]:
        return await self._execute(lambda value: self.uow.applicant_profiles.replace_educations(value.applicant_id, value.items), command)


class ReplaceLanguageSkillsHandler(_BaseHandler[ReplaceLanguageSkillsCommand, list[LanguageSkill]]):
    async def handle(self, command: ReplaceLanguageSkillsCommand) -> list[LanguageSkill]:
        return await self._execute(lambda value: self.uow.applicant_profiles.replace_language_skills(value.applicant_id, value.items), command)


class ReplaceJobPreferenceHandler(_BaseHandler[ReplaceJobPreferenceCommand, JobPreference]):
    async def handle(self, command: ReplaceJobPreferenceCommand) -> JobPreference:
        return await self._execute(lambda value: self.uow.applicant_profiles.replace_job_preference(value.applicant_id, value.item), command)

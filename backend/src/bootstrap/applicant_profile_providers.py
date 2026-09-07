from application.applicant_profile.handlers.update_profile_components import (
    ReplaceEducationsHandler, ReplaceJobPreferenceHandler, ReplaceLanguageSkillsHandler,
    ReplaceSkillsHandler, ReplaceWorkExperiencesHandler,
)
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_skills_handler() -> ReplaceSkillsHandler:
    return ReplaceSkillsHandler(get_uow())


def provide_work_experiences_handler() -> ReplaceWorkExperiencesHandler:
    return ReplaceWorkExperiencesHandler(get_uow())


def provide_educations_handler() -> ReplaceEducationsHandler:
    return ReplaceEducationsHandler(get_uow())


def provide_language_skills_handler() -> ReplaceLanguageSkillsHandler:
    return ReplaceLanguageSkillsHandler(get_uow())


def provide_job_preference_handler() -> ReplaceJobPreferenceHandler:
    return ReplaceJobPreferenceHandler(get_uow())

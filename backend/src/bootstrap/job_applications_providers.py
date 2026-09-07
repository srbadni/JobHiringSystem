from application.job_applications.handlers.create_job_application_handler import CreateJobApplicationHandler
from application.job_applications.handlers.get_job_application_handler import GetJobApplicationHandler
from application.job_applications.handlers.list_my_job_applications_handler import ListMyJobApplicationsHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_job_application_handler() -> CreateJobApplicationHandler:
    return CreateJobApplicationHandler(uow=get_uow())


def provide_list_my_job_applications_handler() -> ListMyJobApplicationsHandler:
    return ListMyJobApplicationsHandler(uow=get_uow())


def provide_get_job_application_handler() -> GetJobApplicationHandler:
    return GetJobApplicationHandler(uow=get_uow())

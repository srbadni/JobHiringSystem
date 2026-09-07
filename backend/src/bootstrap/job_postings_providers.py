from application.job_management.handlers.create_job_posting_handler import CreateJobPostingHandler
from application.job_management.handlers.delete_job_posting_handler import DeleteJobPostingHandler
from application.job_management.handlers.get_job_posting_by_id_handler import GetJobPostingByIdQueryHandler
from application.job_management.handlers.list_job_postings_handler import ListJobPostingsQueryHandler
from application.job_management.handlers.update_job_posting_handler import UpdateJobPostingHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_job_posting_handler() -> CreateJobPostingHandler:
    return CreateJobPostingHandler(
        uow=get_uow(),
    )


def provide_list_job_postings_handler() -> ListJobPostingsQueryHandler:
    return ListJobPostingsQueryHandler(uow=get_uow())


def provide_get_job_posting_by_id_handler() -> GetJobPostingByIdQueryHandler:
    return GetJobPostingByIdQueryHandler(uow=get_uow())


def provide_update_job_posting_handler() -> UpdateJobPostingHandler:
    return UpdateJobPostingHandler(uow=get_uow())


def provide_delete_job_posting_handler() -> DeleteJobPostingHandler:
    return DeleteJobPostingHandler(uow=get_uow())

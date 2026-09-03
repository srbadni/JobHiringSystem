from application.job_posting.handlers.create_job_posting_handler import CreateJobPostingHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_job_posting_handler() -> CreateJobPostingHandler:
    return CreateJobPostingHandler(
        uow=get_uow(),
    )
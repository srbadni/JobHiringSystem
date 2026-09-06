from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_jobs_result_handler() -> GetJobsQueryHandler:
    return GetJobsQueryHandler(
        uow=get_uow()
    )
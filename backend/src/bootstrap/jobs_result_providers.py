from application.jobs_search.handlers.get_company_jobs_handler import GetCompanyJobsHandler
from application.jobs_search.handlers.get_company_details_handler import GetCompanyDetailsHandler
from application.jobs_search.handlers.get_job_details_handler import GetJobDetailsHandler
from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_jobs_result_handler() -> GetJobsQueryHandler:
    return GetJobsQueryHandler(
        uow=get_uow()
    )

def provide_company_jobs_result_handler() -> GetCompanyJobsHandler:
    return GetCompanyJobsHandler(
        uow=get_uow()
    )

def provide_company_details_handler() -> GetCompanyDetailsHandler:
    return GetCompanyDetailsHandler(
        uow=get_uow()
    )

def provide_job_details_handler() -> GetJobDetailsHandler:
    return GetJobDetailsHandler(
        uow=get_uow()
    )

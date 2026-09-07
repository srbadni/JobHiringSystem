from application.company_activities.handlers.create_company_activity_handler import CreateCompanyActivityHandler
from application.company_activities.handlers.delete_company_activity_handler import DeleteCompanyActivityHandler
from application.company_activities.handlers.get_company_activity_by_id_handler import GetCompanyActivityByIdQueryHandler
from application.company_activities.handlers.list_company_activities_handler import ListCompanyActivitiesQueryHandler
from application.company_activities.handlers.update_company_activity_handler import UpdateCompanyActivityHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_company_activity_handler() -> CreateCompanyActivityHandler:
    return CreateCompanyActivityHandler(uow=get_uow())


def provide_list_company_activities_handler() -> ListCompanyActivitiesQueryHandler:
    return ListCompanyActivitiesQueryHandler(uow=get_uow())


def provide_get_company_activity_by_id_handler() -> GetCompanyActivityByIdQueryHandler:
    return GetCompanyActivityByIdQueryHandler(uow=get_uow())


def provide_update_company_activity_handler() -> UpdateCompanyActivityHandler:
    return UpdateCompanyActivityHandler(uow=get_uow())


def provide_delete_company_activity_handler() -> DeleteCompanyActivityHandler:
    return DeleteCompanyActivityHandler(uow=get_uow())

from application.salary_ranges.handlers.create_salary_range_handler import CreateSalaryRangeHandler
from application.salary_ranges.handlers.delete_salary_range_handler import DeleteSalaryRangeHandler
from application.salary_ranges.handlers.get_salary_range_by_id_handler import GetSalaryRangeByIdQueryHandler
from application.salary_ranges.handlers.list_salary_ranges_handler import ListSalaryRangesQueryHandler
from application.salary_ranges.handlers.update_salary_range_handler import UpdateSalaryRangeHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_salary_range_handler() -> CreateSalaryRangeHandler:
    return CreateSalaryRangeHandler(uow=get_uow())


def provide_list_salary_ranges_handler() -> ListSalaryRangesQueryHandler:
    return ListSalaryRangesQueryHandler(uow=get_uow())


def provide_get_salary_range_by_id_handler() -> GetSalaryRangeByIdQueryHandler:
    return GetSalaryRangeByIdQueryHandler(uow=get_uow())


def provide_update_salary_range_handler() -> UpdateSalaryRangeHandler:
    return UpdateSalaryRangeHandler(uow=get_uow())


def provide_delete_salary_range_handler() -> DeleteSalaryRangeHandler:
    return DeleteSalaryRangeHandler(uow=get_uow())

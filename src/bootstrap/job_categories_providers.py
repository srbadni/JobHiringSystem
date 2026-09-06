from application.job_categories.handlers.create_job_category_handler import CreateJobCategoryHandler
from application.job_categories.handlers.delete_job_category_handler import DeleteJobCategoryHandler
from application.job_categories.handlers.get_job_category_by_id_handler import GetJobCategoryByIdQueryHandler
from application.job_categories.handlers.list_job_categories_handler import ListJobCategoriesQueryHandler
from application.job_categories.handlers.update_job_category_handler import UpdateJobCategoryHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_create_job_category_handler() -> CreateJobCategoryHandler:
    return CreateJobCategoryHandler(uow=get_uow())


def provide_list_job_categories_handler() -> ListJobCategoriesQueryHandler:
    return ListJobCategoriesQueryHandler(uow=get_uow())


def provide_get_job_category_by_id_handler() -> GetJobCategoryByIdQueryHandler:
    return GetJobCategoryByIdQueryHandler(uow=get_uow())


def provide_update_job_category_handler() -> UpdateJobCategoryHandler:
    return UpdateJobCategoryHandler(uow=get_uow())


def provide_delete_job_category_handler() -> DeleteJobCategoryHandler:
    return DeleteJobCategoryHandler(uow=get_uow())

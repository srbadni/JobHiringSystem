from application.locations.handlers.list_cities_handler import ListCitiesQueryHandler
from application.locations.handlers.list_provinces_handler import ListProvincesQueryHandler
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow


def provide_list_provinces_handler() -> ListProvincesQueryHandler:
    return ListProvincesQueryHandler(uow=get_uow())


def provide_list_cities_handler() -> ListCitiesQueryHandler:
    return ListCitiesQueryHandler(uow=get_uow())

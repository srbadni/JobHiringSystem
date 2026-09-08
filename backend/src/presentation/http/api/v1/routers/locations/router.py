# pyright: reportUnusedFunction=false

from collections.abc import Callable
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from application.locations.handlers.list_cities_handler import ListCitiesQueryHandler
from application.locations.handlers.list_provinces_handler import ListProvincesQueryHandler
from application.locations.query.list_cities import ListCitiesQuery
from application.locations.query.list_provinces import ListProvincesQuery

from .schemas import CityRead, ProvinceRead

ListProvincesHandlerProvider = Callable[[], ListProvincesQueryHandler]
ListCitiesHandlerProvider = Callable[[], ListCitiesQueryHandler]


def create_locations_router(
    provide_list_provinces_handler: ListProvincesHandlerProvider,
    provide_list_cities_handler: ListCitiesHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Public - Locations"])

    @router.get("/provinces", response_model=list[ProvinceRead])
    async def list_provinces(
        handler: Annotated[
            ListProvincesQueryHandler,
            Depends(provide_list_provinces_handler),
        ],
    ):
        return await handler.handle(ListProvincesQuery())

    @router.get("/cities", response_model=list[CityRead])
    async def list_cities(
        handler: Annotated[
            ListCitiesQueryHandler,
            Depends(provide_list_cities_handler),
        ],
        province_id: Annotated[UUID | None, Query()] = None,
    ):
        return await handler.handle(ListCitiesQuery(province_id=province_id))

    return router

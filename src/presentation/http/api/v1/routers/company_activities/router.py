# pyright: reportUnusedFunction=false

from typing import Annotated, Callable
from uuid import UUID

from fastapi import APIRouter, Depends, status

from application.company_activities.command.create_company_activity import CreateCompanyActivityCommand
from application.company_activities.command.delete_company_activity import DeleteCompanyActivityCommand
from application.company_activities.command.update_company_activity import UpdateCompanyActivityCommand
from application.company_activities.handlers.create_company_activity_handler import CreateCompanyActivityHandler
from application.company_activities.handlers.delete_company_activity_handler import DeleteCompanyActivityHandler
from application.company_activities.handlers.get_company_activity_by_id_handler import GetCompanyActivityByIdQueryHandler
from application.company_activities.handlers.list_company_activities_handler import ListCompanyActivitiesQueryHandler
from application.company_activities.handlers.update_company_activity_handler import UpdateCompanyActivityHandler
from application.company_activities.query.get_company_activity_by_id import GetCompanyActivityByIdQuery
from application.company_activities.query.list_company_activities import ListCompanyActivitiesQuery

from .schemas import CompanyActivityCreate, CompanyActivityRead, CompanyActivityUpdate

CreateHandlerProvider = Callable[[], CreateCompanyActivityHandler]
ListHandlerProvider = Callable[[], ListCompanyActivitiesQueryHandler]
GetByIdHandlerProvider = Callable[[], GetCompanyActivityByIdQueryHandler]
UpdateHandlerProvider = Callable[[], UpdateCompanyActivityHandler]
DeleteHandlerProvider = Callable[[], DeleteCompanyActivityHandler]


def create_company_activities_router(
    provide_create_handler: CreateHandlerProvider,
    provide_list_handler: ListHandlerProvider,
    provide_get_by_id_handler: GetByIdHandlerProvider,
    provide_update_handler: UpdateHandlerProvider,
    provide_delete_handler: DeleteHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Admin - Company Activities"])

    @router.post("", status_code=status.HTTP_201_CREATED, response_model=CompanyActivityRead)
    async def create_company_activity(
        data: CompanyActivityCreate,
        handler: Annotated[CreateCompanyActivityHandler, Depends(provide_create_handler)],
    ):
        return await handler.handle(CreateCompanyActivityCommand(
            code=data.code,
            title=data.title,
        ))

    @router.get("", response_model=list[CompanyActivityRead])
    async def list_company_activities(
        handler: Annotated[ListCompanyActivitiesQueryHandler, Depends(provide_list_handler)],
    ):
        return await handler.handle(ListCompanyActivitiesQuery())

    @router.get("/{activity_id}", response_model=CompanyActivityRead)
    async def get_company_activity(
        activity_id: UUID,
        handler: Annotated[GetCompanyActivityByIdQueryHandler, Depends(provide_get_by_id_handler)],
    ):
        return await handler.handle(GetCompanyActivityByIdQuery(company_activity_id=activity_id))

    @router.put("/{activity_id}", response_model=CompanyActivityRead)
    async def update_company_activity(
        activity_id: UUID,
        data: CompanyActivityUpdate,
        handler: Annotated[UpdateCompanyActivityHandler, Depends(provide_update_handler)],
    ):
        return await handler.handle(UpdateCompanyActivityCommand(
            company_activity_id=activity_id,
            code=data.code,
            title=data.title,
        ))

    @router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_company_activity(
        activity_id: UUID,
        handler: Annotated[DeleteCompanyActivityHandler, Depends(provide_delete_handler)],
    ) -> None:
        await handler.handle(DeleteCompanyActivityCommand(company_activity_id=activity_id))

    return router

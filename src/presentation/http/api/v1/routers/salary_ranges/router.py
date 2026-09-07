# pyright: reportUnusedFunction=false

from typing import Annotated, Callable
from uuid import UUID

from fastapi import APIRouter, Depends, status

from application.salary_ranges.command.create_salary_range import CreateSalaryRangeCommand
from application.salary_ranges.command.delete_salary_range import DeleteSalaryRangeCommand
from application.salary_ranges.command.update_salary_range import UpdateSalaryRangeCommand
from application.salary_ranges.handlers.create_salary_range_handler import CreateSalaryRangeHandler
from application.salary_ranges.handlers.delete_salary_range_handler import DeleteSalaryRangeHandler
from application.salary_ranges.handlers.get_salary_range_by_id_handler import GetSalaryRangeByIdQueryHandler
from application.salary_ranges.handlers.list_salary_ranges_handler import ListSalaryRangesQueryHandler
from application.salary_ranges.handlers.update_salary_range_handler import UpdateSalaryRangeHandler
from application.salary_ranges.query.get_salary_range_by_id import GetSalaryRangeByIdQuery
from application.salary_ranges.query.list_salary_ranges import ListSalaryRangesQuery

from .schemas import SalaryRangeCreate, SalaryRangeRead, SalaryRangeUpdate

CreateHandlerProvider = Callable[[], CreateSalaryRangeHandler]
ListHandlerProvider = Callable[[], ListSalaryRangesQueryHandler]
GetByIdHandlerProvider = Callable[[], GetSalaryRangeByIdQueryHandler]
UpdateHandlerProvider = Callable[[], UpdateSalaryRangeHandler]
DeleteHandlerProvider = Callable[[], DeleteSalaryRangeHandler]


def create_salary_ranges_router(
    provide_create_handler: CreateHandlerProvider,
    provide_list_handler: ListHandlerProvider,
    provide_get_by_id_handler: GetByIdHandlerProvider,
    provide_update_handler: UpdateHandlerProvider,
    provide_delete_handler: DeleteHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["SalaryRanges"])

    @router.post("", status_code=status.HTTP_201_CREATED, response_model=SalaryRangeRead)
    async def create_salary_range(
        data: SalaryRangeCreate,
        handler: Annotated[CreateSalaryRangeHandler, Depends(provide_create_handler)],
    ):
        return await handler.handle(CreateSalaryRangeCommand(
            title=data.title,
            min_salary=data.min_salary,
            max_salary=data.max_salary,
        ))

    @router.get("", response_model=list[SalaryRangeRead])
    async def list_salary_ranges(
        handler: Annotated[ListSalaryRangesQueryHandler, Depends(provide_list_handler)],
    ):
        return await handler.handle(ListSalaryRangesQuery())

    @router.get("/{salary_range_id}", response_model=SalaryRangeRead)
    async def get_salary_range(
        salary_range_id: UUID,
        handler: Annotated[GetSalaryRangeByIdQueryHandler, Depends(provide_get_by_id_handler)],
    ):
        return await handler.handle(GetSalaryRangeByIdQuery(salary_range_id=salary_range_id))

    @router.put("/{salary_range_id}", response_model=SalaryRangeRead)
    async def update_salary_range(
        salary_range_id: UUID,
        data: SalaryRangeUpdate,
        handler: Annotated[UpdateSalaryRangeHandler, Depends(provide_update_handler)],
    ):
        return await handler.handle(UpdateSalaryRangeCommand(
            salary_range_id=salary_range_id,
            title=data.title,
            min_salary=data.min_salary,
            max_salary=data.max_salary,
        ))

    @router.delete("/{salary_range_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_salary_range(
        salary_range_id: UUID,
        handler: Annotated[DeleteSalaryRangeHandler, Depends(provide_delete_handler)],
    ) -> None:
        await handler.handle(DeleteSalaryRangeCommand(salary_range_id=salary_range_id))

    return router

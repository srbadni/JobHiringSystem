# pyright: reportUnusedFunction=false

from typing import Annotated, Callable
from uuid import UUID

from fastapi import APIRouter, Depends, status

from application.job_categories.command.create_job_category import CreateJobCategoryCommand
from application.job_categories.command.delete_job_category import DeleteJobCategoryCommand
from application.job_categories.command.update_job_category import UpdateJobCategoryCommand
from application.job_categories.handlers.create_job_category_handler import CreateJobCategoryHandler
from application.job_categories.handlers.delete_job_category_handler import DeleteJobCategoryHandler
from application.job_categories.handlers.get_job_category_by_id_handler import GetJobCategoryByIdQueryHandler
from application.job_categories.handlers.list_job_categories_handler import ListJobCategoriesQueryHandler
from application.job_categories.handlers.update_job_category_handler import UpdateJobCategoryHandler
from application.job_categories.query.get_job_category_by_id import GetJobCategoryByIdQuery
from application.job_categories.query.list_job_categories import ListJobCategoriesQuery

from .schemas import JobCategoryCreate, JobCategoryRead, JobCategoryUpdate

CreateHandlerProvider = Callable[[], CreateJobCategoryHandler]
ListHandlerProvider = Callable[[], ListJobCategoriesQueryHandler]
GetByIdHandlerProvider = Callable[[], GetJobCategoryByIdQueryHandler]
UpdateHandlerProvider = Callable[[], UpdateJobCategoryHandler]
DeleteHandlerProvider = Callable[[], DeleteJobCategoryHandler]


def create_job_categories_router(
    provide_create_handler: CreateHandlerProvider,
    provide_list_handler: ListHandlerProvider,
    provide_get_by_id_handler: GetByIdHandlerProvider,
    provide_update_handler: UpdateHandlerProvider,
    provide_delete_handler: DeleteHandlerProvider,
) -> APIRouter:
    router = APIRouter(tags=["Job Categories"])

    @router.post("", status_code=status.HTTP_201_CREATED, response_model=JobCategoryRead)
    async def create_job_category(
        data: JobCategoryCreate,
        handler: Annotated[CreateJobCategoryHandler, Depends(provide_create_handler)],
    ):
        return await handler.handle(CreateJobCategoryCommand(
            code=data.code,
            title=data.title,
        ))

    @router.get("", response_model=list[JobCategoryRead])
    async def list_job_categories(
        handler: Annotated[ListJobCategoriesQueryHandler, Depends(provide_list_handler)],
    ):
        return await handler.handle(ListJobCategoriesQuery())

    @router.get("/{category_id}", response_model=JobCategoryRead)
    async def get_job_category(
        category_id: UUID,
        handler: Annotated[GetJobCategoryByIdQueryHandler, Depends(provide_get_by_id_handler)],
    ):
        return await handler.handle(GetJobCategoryByIdQuery(job_category_id=category_id))

    @router.put("/{category_id}", response_model=JobCategoryRead)
    async def update_job_category(
        category_id: UUID,
        data: JobCategoryUpdate,
        handler: Annotated[UpdateJobCategoryHandler, Depends(provide_update_handler)],
    ):
        return await handler.handle(UpdateJobCategoryCommand(
            job_category_id=category_id,
            code=data.code,
            title=data.title,
        ))

    @router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_job_category(
        category_id: UUID,
        handler: Annotated[DeleteJobCategoryHandler, Depends(provide_delete_handler)],
    ) -> None:
        await handler.handle(DeleteJobCategoryCommand(job_category_id=category_id))

    return router

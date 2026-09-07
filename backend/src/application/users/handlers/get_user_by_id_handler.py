from domain.user.models import User

from ...common.ports.unit_of_work import UnitOfWork
from ..query.get_user_by_id import GetUserByIdQuery


class GetUserByIdQueryHandler:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, query: GetUserByIdQuery) -> User:
        async with self.uow:
            return await self.uow.users.get_by_id(query.user_id)

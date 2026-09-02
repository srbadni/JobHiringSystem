from domain.user.models import User

from ...common.ports.unit_of_work import UnitOfWork
from ..query.list_users import ListUsersQuery


class ListUsersQueryHandler:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, query: ListUsersQuery) -> list[User]:
        async with self.uow:
            return await self.uow.users.list()

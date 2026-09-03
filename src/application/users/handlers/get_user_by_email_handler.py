from domain.user.models import User

from ...common.ports.unit_of_work import UnitOfWork
from ..query.get_user_by_email import GetUserByEmailQuery


class GetUserByEmailQueryHandler:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, query: GetUserByEmailQuery) -> User:
        async with self.uow:
            return await self.uow.users.get_by_email(query.email)

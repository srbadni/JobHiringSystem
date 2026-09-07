from application.common.ports.unit_of_work import UnitOfWork
from ..command.delete_user import DeleteUserCommand


class DeleteUserCommandHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: DeleteUserCommand) -> None:
        async with self.uow:
            await self.uow.users.delete(command.user_id)
            await self.uow.commit()

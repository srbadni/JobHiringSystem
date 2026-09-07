from application.common.ports.unit_of_work import UnitOfWork
from domain.user.models import User
from ..command.update_user import UpdateUserCommand


class UpdateUserCommandHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: UpdateUserCommand) -> User:
        async with self.uow:
            current = await self.uow.users.get_by_id(command.user_id)
            current.full_name = command.full_name
            current.phone_number = command.phone_number
            current.email = command.email
            current.profile_image_url = command.profile_image_url
            result = await self.uow.users.update(current)
            await self.uow.commit()
            return result

from fastapi import HTTPException
from domain.user.models import User
from ..ports.user_repository import UserRepository
from ..command.create_user import CreateUserCommand
from ...common.ports.password_hasher import PasswordHasher


class CreateUserCommandHandler:

    def __init__(self, repository: UserRepository, hasher: PasswordHasher):
        self.repository = repository
        self.hasher = hasher

    async def handle(self, command: CreateUserCommand) -> User:
        hashed_password = self.hasher.hash(command.password)

        exists = await self.repository.exists_by_email(command.email)
        if exists:
            raise HTTPException

        user = User(
            full_name=command.full_name,
            phone_number=command.phone_number,
            email=command.email,
            hashed_password=hashed_password,
        )

        return await self.repository.add(user)



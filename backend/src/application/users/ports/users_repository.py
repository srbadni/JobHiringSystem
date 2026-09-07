from abc import ABC, abstractmethod

from domain.user.models import User
from domain.user.enums import UserType
from uuid import UUID


class UsersRepository(ABC):

    @abstractmethod
    async def list(self, user_type: UserType | None = None) -> list[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def add(self, user: User) -> User:
        pass

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, user_id: UUID) -> None:
        pass

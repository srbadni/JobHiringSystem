from abc import ABC, abstractmethod

from domain.user.models import User


class UsersRepository(ABC):

    @abstractmethod
    async def list(self) -> list[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: str) -> User:
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
from abc import ABC, abstractmethod

from ...users.ports.users_repository import UsersRepository


class UnitOfWork(ABC):
    users: UsersRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass
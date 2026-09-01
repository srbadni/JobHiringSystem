from abc import ABC, abstractmethod
from ...users.ports.users_repository import UsersRepository


class UnitOfWork(ABC):
    users: UsersRepository

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass
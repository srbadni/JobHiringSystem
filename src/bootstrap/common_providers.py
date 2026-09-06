from application.common.ports.unit_of_work import UnitOfWork
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal
from infrastructure.persistence.sqlalchemy.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.security.pwdlib_password_hasher import PwdlibPasswordHasher


password_hasher = PwdlibPasswordHasher()


def provide_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(
        session_factory=AsyncSessionLocal,
    )

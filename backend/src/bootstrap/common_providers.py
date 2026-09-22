from application.authentication.ports.authentication import IAuthentication, UserClaims
from application.common.ports.unit_of_work import UnitOfWork
from infrastructure.authentication.jwt_authentication import JWTAuthentication
from infrastructure.persistence.sqlalchemy.session import AsyncSessionLocal
from infrastructure.persistence.sqlalchemy.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.security.pwdlib_password_hasher import PwdlibPasswordHasher
from presentation.http.api.dependencies.authentication import build_current_user_dependency

password_hasher = PwdlibPasswordHasher()

def provide_auth() -> IAuthentication:
    return JWTAuthentication()

def provide_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork(
        session_factory=AsyncSessionLocal,
    )

def provide_get_current_user(access_token: str) -> UserClaims:
    auth = provide_auth()
    return auth.get_current_user(access_token)

current_user_dependency = build_current_user_dependency(
    authenticate_user=provide_get_current_user,
)
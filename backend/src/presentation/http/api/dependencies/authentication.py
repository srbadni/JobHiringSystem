from collections.abc import Callable
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from application.authentication.exceptions import InvalidAccessTokenError
from application.authentication.ports.authentication import UserClaims


AuthenticateUser = Callable[[str], UserClaims]
CurrentUserDependency = Callable[..., UserClaims]

bearer_scheme = HTTPBearer(auto_error=False)


def build_current_user_dependency(
    authenticate_user: AuthenticateUser,
) -> CurrentUserDependency:

    def get_current_user(
        credentials: Annotated[
            HTTPAuthorizationCredentials | None,
            Depends(bearer_scheme),
        ],
    ) -> UserClaims:
        unauthorized = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        if credentials is None:
            raise unauthorized

        try:
            return authenticate_user(credentials.credentials)
        except InvalidAccessTokenError as exc:
            raise unauthorized from exc

    return get_current_user
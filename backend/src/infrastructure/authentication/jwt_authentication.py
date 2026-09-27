from datetime import timedelta, datetime, timezone

import jwt
from jwt import InvalidTokenError

from application.authentication.exceptions import InvalidAccessTokenError
from application.authentication.ports.authentication import IAuthentication, UserJWTData, UserClaims
from infrastructure.config import settings


class JWTAuthentication(IAuthentication):

    def create_access_token(self, data: UserJWTData, expires_delta: timedelta | None = timedelta(minutes=settings.jwt_access_token_expire_minutes)) -> str:
        to_encode = {
            "user_id": str(data.user_id)
        }
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
        return encoded_jwt

    def get_current_user(self, access_token: str) -> UserClaims:
        try:
            decode = jwt.decode(access_token, settings.jwt_secret_key, algorithms=settings.jwt_algorithm)
        except InvalidTokenError as exc:
            raise InvalidAccessTokenError() from exc
        return decode
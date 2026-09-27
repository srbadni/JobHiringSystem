from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, TypedDict
from uuid import UUID

class UserClaims(TypedDict):
    user_id: str
    exp: int

@dataclass
class UserJWTData:
    user_id: UUID

class IAuthentication(ABC):

    @abstractmethod
    def create_access_token(self, data: UserJWTData, expires_delta: timedelta | None = None):
        pass

    @abstractmethod
    def get_current_user(self, access_token: str) -> UserClaims:
        pass
from dataclasses import dataclass
from domain.user.enums import UserType


@dataclass(frozen=True, slots=True)
class ListUsersQuery:
    user_type: UserType | None = None

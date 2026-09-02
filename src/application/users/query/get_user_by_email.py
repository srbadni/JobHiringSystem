from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GetUserByEmailQuery:
    email: str

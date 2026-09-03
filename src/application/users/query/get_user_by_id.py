from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GetUserByIdQuery:
    user_id: str

from dataclasses import dataclass


@dataclass
class GetCurrentUserQuery:
    access_token: str
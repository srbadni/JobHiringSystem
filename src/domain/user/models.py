from dataclasses import dataclass, field
from uuid import uuid4, UUID

from .enums import UserType


@dataclass(slots=True)
class User:
    full_name: str
    phone_number: str
    email: str
    hashed_password: str

    id: UUID = field(default_factory=uuid4)
    user_type: UserType = UserType.APPLICANT
    is_superuser: bool = False
    email_verified: bool = False
    profile_image_url: str | None = None
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class UpdateUserCommand:
    user_id: UUID
    full_name: str
    phone_number: str
    email: str
    profile_image_url: str | None = None

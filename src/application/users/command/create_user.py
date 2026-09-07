from dataclasses import dataclass
from domain.user.enums import UserType


@dataclass
class CreateUserCommand:
    full_name: str
    phone_number: str
    email: str
    password: str
    profile_image_url: str | None = None
    user_type: UserType = UserType.APPLICANT

from dataclasses import dataclass

from domain.user.enums import UserType


@dataclass
class CreateUserCommand:
    full_name: str
    phone_number: str
    email: str
    password: str
    user_type: UserType = UserType.APPLICANT
    profile_image_url: str | None = None

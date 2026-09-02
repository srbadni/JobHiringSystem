from dataclasses import dataclass


@dataclass
class CreateUserCommand:
    full_name: str
    phone_number: str
    email: str
    password: str
    profile_image_url: str | None = None

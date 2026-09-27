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
    is_profile_completed: bool = False

    def update_profile_completion(self, *, has_company_membership: bool) -> None:
        if self.user_type == UserType.EMPLOYER:
            if has_company_membership:
                self.is_profile_completed = True
                return
            self.is_profile_completed = False
            return
        else:
            self.is_profile_completed = True
            return

    @classmethod
    def create(
            cls,
            full_name: str,
            phone_number: str,
            email: str,
            hashed_password: str,
            profile_image_url: str | None,
            user_type: UserType = UserType.APPLICANT,
    ) -> User:

        return cls(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            hashed_password=hashed_password,
            profile_image_url=profile_image_url,
            user_type=user_type,
        )

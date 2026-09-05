from fastapi import HTTPException

from domain.applicant_profile.models import ApplicantProfile
from domain.user.models import User
from domain.user.enums import UserType
from ..command.create_user import CreateUserCommand
from ...common.ports.password_hasher import PasswordHasher
from ...common.ports.unit_of_work import UnitOfWork


class CreateUserCommandHandler:

    def __init__(self, uow: UnitOfWork, hasher: PasswordHasher):
        self.uow = uow
        self.hasher = hasher

    async def handle(self, command: CreateUserCommand) -> User:
        async with self.uow:
            hashed_password = self.hasher.hash(command.password)

            exists = await self.uow.users.exists_by_email(command.email)
            if exists:
                raise HTTPException(
                    status_code=409,
                    detail="A user with this email already exists.",
                )

            user = User(
                full_name=command.full_name,
                phone_number=command.phone_number,
                email=command.email,
                hashed_password=hashed_password,
                user_type=UserType.APPLICANT,
                profile_image_url=command.profile_image_url,
            )

            result = await self.uow.users.add(user)
            await self.uow.applicant_profiles.add(ApplicantProfile(
                applicant_id=result.id,
            ))

            await self.uow.commit()

            return result



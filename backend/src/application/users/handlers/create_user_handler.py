from domain.applicant_profile.models import ApplicantProfile
from domain.user.models import User
from domain.user.exceptions import UserAlreadyExistsError
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
                raise UserAlreadyExistsError("A user with this email already exists.")

            user = User.create(
                full_name=command.full_name,
                phone_number=command.phone_number,
                email=command.email,
                hashed_password=hashed_password,
                profile_image_url=command.profile_image_url,
                user_type=command.user_type,
            )

            result = await self.uow.users.add(user)
            if command.user_type.value == "applicant":
                await self.uow.applicant_profiles.add(ApplicantProfile(applicant_id=result.id))

            await self.uow.commit()

            return result


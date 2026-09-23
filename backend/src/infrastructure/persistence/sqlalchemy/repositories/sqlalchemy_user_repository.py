from sqlalchemy import select, exists
from uuid import UUID
from domain.user.enums import UserType
from domain.user.exceptions import UserNotFoundError
from sqlalchemy.ext.asyncio import AsyncSession

from application.users.ports.users_repository import UsersRepository
from domain.user.models import User
from infrastructure.persistence.sqlalchemy.models.user import User as UserModel


class SqlAlchemyUsersRepository(UsersRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            full_name=model.full_name,
            phone_number=model.phone_number,
            hashed_password=model.hashed_password,
            user_type=model.user_type,
            is_superuser=model.is_superuser,
            email_verified=model.email_verified,
            profile_image_url=model.profile_image_url,
        )

    async def list(self, user_type: UserType | None = None) -> list[User]:
        statement = select(UserModel)
        if user_type is not None:
            statement = statement.where(UserModel.user_type == user_type)
        result = await self.session.scalars(statement)
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, user_id: UUID) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.id == user_id)
        )
        return self._to_domain(result.one())

    async def get_by_email(self, email: str) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.email == email)
        )
        return self._to_domain(result.one())

    async def get_applicant_by_email(self, email: str) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.email == email, UserModel.user_type == UserType.APPLICANT)
        )
        return self._to_domain(result.one())

    async def get_employer_by_email(self, email: str) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.email == email, UserModel.user_type == UserType.EMPLOYER)
        )
        return self._to_domain(result.one())

    async def exists_by_email(self, email: str) -> bool:
        stmt = select(
            exists().where(UserModel.email == email)
        )

        return bool(await self.session.scalar(stmt))

    async def add(self, user: User) -> User:

        model = UserModel(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            phone_number=user.phone_number,
            hashed_password=user.hashed_password,
            user_type=user.user_type,
            profile_image_url=user.profile_image_url
        )

        self.session.add(model)
        await self.session.flush()

        return self._to_domain(model)

    async def update(self, user: User) -> User:
        model = await self.session.get(UserModel, user.id)
        if model is None:
            raise UserNotFoundError("User was not found")
        model.full_name = user.full_name
        model.phone_number = user.phone_number
        model.email = user.email
        model.profile_image_url = user.profile_image_url
        # Account type is deliberately immutable through admin updates.
        await self.session.flush()
        return self._to_domain(model)

    async def delete(self, user_id: UUID) -> None:
        model = await self.session.get(UserModel, user_id)
        if model is None:
            raise UserNotFoundError("User was not found")
        await self.session.delete(model)
        await self.session.flush()

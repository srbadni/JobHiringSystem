from sqlalchemy import select, exists
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

    async def list(self) -> list[User]:
        result = await self.session.scalars(select(UserModel))
        return [self._to_domain(model) for model in result.all()]

    async def get_by_id(self, user_id: str) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.id == user_id)
        )
        return self._to_domain(result.one())

    async def get_by_email(self, email: str) -> User:
        result = await self.session.scalars(
            select(UserModel).where(UserModel.email == email)
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

        return self._to_domain(model)

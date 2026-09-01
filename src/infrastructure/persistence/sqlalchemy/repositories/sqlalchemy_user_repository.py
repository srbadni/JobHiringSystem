from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from application.users.ports.users_repository import UsersRepository
from domain.user.models import User
from infrastructure.persistence.sqlalchemy.models.user import User as UserModel


class SqlAlchemyUsersRepository(UsersRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

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

        return User(
            id=model.id,
            email=model.email,
            full_name=model.full_name,
            phone_number=model.phone_number,
            hashed_password=model.hashed_password,
            user_type=model.user_type,
            profile_image_url=model.profile_image_url
        )
import uuid

from application.authentication.exceptions import UserNotFound, InvalidAccessTokenError
from application.authentication.ports.authentication import IAuthentication
from application.authentication.query.get_current_user import GetCurrentUserQuery
from application.common.ports.unit_of_work import UnitOfWork
from domain.user.models import User


class GetCurrentUserHandler:

    def __init__(self, auth: IAuthentication, uow: UnitOfWork):
        self.auth = auth
        self.uow = uow

    async def handle(self, query: GetCurrentUserQuery) -> User:
        async with self.uow:
            try:
                user_info = self.auth.get_current_user(
                    query.access_token
                )
            except InvalidAccessTokenError:
                raise UserNotFound

            user_from_db = await self.uow.users.get_by_id(uuid.UUID(user_info["user_id"]))
            if not user_from_db:
                raise UserNotFound

            company_membership = await self.uow.company_memberships.get_by_user_id(user_from_db.id)
            user_from_db.update_profile_completion(has_company_membership=bool(company_membership))

            return User(
                id=user_from_db.id,
                full_name=user_from_db.full_name,
                phone_number=user_from_db.phone_number,
                email=user_from_db.email,
                user_type=user_from_db.user_type,
                profile_image_url=user_from_db.profile_image_url,
                hashed_password=user_from_db.hashed_password,
                is_profile_completed=user_from_db.is_profile_completed,
            )
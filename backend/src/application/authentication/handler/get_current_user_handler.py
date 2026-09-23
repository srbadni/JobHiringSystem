import uuid

from application.authentication.ports.authentication import IAuthentication
from application.authentication.query.get_current_user import GetCurrentUserQuery
from application.common.ports.unit_of_work import UnitOfWork


class GetCurrentUserHandler:

    def __init__(self, auth: IAuthentication, uow: UnitOfWork):
        self.auth = auth
        self.uow = uow

    async def handle(self, query: GetCurrentUserQuery):
        async with self.uow:
            user_info = self.auth.get_current_user(
                query.access_token
            )
            user_from_db = await self.uow.users.get_by_id(uuid.UUID(user_info["user_id"]))
            return {
                "id": user_from_db.id,
                "full_name": user_from_db.full_name,
                "phone_number": user_from_db.phone_number,
                "email": user_from_db.email,
                "user_type": user_from_db.user_type,
                "profile_image_url": user_from_db.profile_image_url,
            }
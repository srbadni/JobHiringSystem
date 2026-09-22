from application.authentication.command.login import LoginCommand
from application.authentication.dto import Token
from application.authentication.ports.authentication import IAuthentication, UserJWTData
from application.common.ports.password_hasher import PasswordHasher
from application.common.ports.unit_of_work import UnitOfWork


class LoginHandler:
    def __init__(self, uow: UnitOfWork, hasher: PasswordHasher, auth: IAuthentication):
        self.uow = uow
        self.hasher = hasher
        self.auth = auth
        pass

    async def handle(self, command: LoginCommand):
        async with self.uow:
            user = await self.uow.users.get_by_email(command.email)
            if not user:
                raise Exception
            hashed_password = self.hasher.hash(command.password)
            if not self.hasher.verify(command.password, hashed_password):
                raise Exception
            return Token(
                access_token=self.auth.create_access_token(UserJWTData(user_id=user.id)),
                token_type="bearer"
            )

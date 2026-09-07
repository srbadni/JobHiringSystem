import unittest
from application.users.command.create_user import CreateUserCommand
from application.users.handlers.create_user_handler import CreateUserCommandHandler
from domain.user.exceptions import UserAlreadyExistsError

class Hasher:
    def hash(self, password: str) -> str: return "hashed"
    def verify(self, password: str, hashed_password: str) -> bool: return True

class Repo:
    def __init__(self, exists=False): self.exists = exists; self.items = []
    async def exists_by_email(self, email): return self.exists
    async def add(self, item): self.items.append(item); return item

class Uow:
    def __init__(self, exists=False):
        self.users = Repo(exists); self.applicant_profiles = Repo(); self.commits = 0; self.rollbacks = 0
    async def __aenter__(self): return self
    async def __aexit__(self, *args): self.rollbacks += 1
    async def commit(self): self.commits += 1

class RegistrationTransactionTests(unittest.IsolatedAsyncioTestCase):
    async def test_applicant_is_created_with_profile_and_one_commit(self):
        uow = Uow()
        result = await CreateUserCommandHandler(uow, Hasher()).handle(CreateUserCommand(
            full_name="Applicant", phone_number="09123456789", email="a@example.test", password="secret"))
        self.assertEqual(result.id, uow.applicant_profiles.items[0].applicant_id)
        self.assertEqual(1, uow.commits)
        self.assertEqual(1, uow.rollbacks)

    async def test_duplicate_rolls_back_without_commit(self):
        uow = Uow(exists=True)
        with self.assertRaises(UserAlreadyExistsError):
            await CreateUserCommandHandler(uow, Hasher()).handle(CreateUserCommand(
                full_name="Applicant", phone_number="09123456789", email="a@example.test", password="secret"))
        self.assertEqual(0, uow.commits)
        self.assertEqual(1, uow.rollbacks)

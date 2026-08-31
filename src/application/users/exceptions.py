class UserAlreadyExistsError(Exception):
    """Raised when a user cannot be created because its email is in use."""

    def __init__(self, email: str) -> None:
        super().__init__(f"A user with email {email!r} already exists")
        self.email = email

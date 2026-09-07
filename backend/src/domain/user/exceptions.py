class UserError(Exception):
    """Base class for expected user-management failures."""


class UserAlreadyExistsError(UserError):
    pass


class UserNotFoundError(UserError):
    pass

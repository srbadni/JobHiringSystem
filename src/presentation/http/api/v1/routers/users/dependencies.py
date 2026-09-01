from application.users.handlers.create_user_handler import CreateUserCommandHandler


def get_create_user_command_handler() -> CreateUserCommandHandler:
    """Dependency hook implemented by the application's composition root."""
    raise RuntimeError("CreateUserCommandHandler has not been configured")

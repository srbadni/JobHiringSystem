from collections.abc import AsyncIterator

from fastapi import Request

from application.users.handlers.create_user_handler import CreateUserCommandHandler


async def get_create_user_handler(
    request: Request,
) -> AsyncIterator[CreateUserCommandHandler]:
    """Resolve a request-scoped handler from the application's container."""
    async with request.app.state.container.create_user_handler() as handler:
        yield handler

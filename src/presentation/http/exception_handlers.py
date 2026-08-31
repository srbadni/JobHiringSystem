from fastapi import Request, status
from fastapi.responses import JSONResponse

from application.users.exceptions import UserAlreadyExistsError


async def user_already_exists_handler(
    request: Request,
    exception: UserAlreadyExistsError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exception)},
    )

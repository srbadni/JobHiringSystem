from application.media.handler.create_media_handler import CreateMediaHandler
from infrastructure.config import settings
from infrastructure.persistence.sqlalchemy.unit_of_work import get_uow
from infrastructure.storage.local_file_storage import LocalFileStorage


file_storage = LocalFileStorage(settings.media_storage_path)


def provide_create_media_handler() -> CreateMediaHandler:
    return CreateMediaHandler(uow=get_uow(), file_storage=file_storage)

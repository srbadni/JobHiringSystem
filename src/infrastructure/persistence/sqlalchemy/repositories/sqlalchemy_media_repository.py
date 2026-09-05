from sqlalchemy.ext.asyncio import AsyncSession

from application.media.dto import MediaDTO
from ..models.media import Media as MediaORMModel
from application.media.ports.media_repository import MediaRepository


class SQLAlchemyMediaRepository(MediaRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, media: MediaDTO) -> MediaDTO:
        model = MediaORMModel(
            original_name=media.original_name,
            storage_key=media.storage_key,
            mime_type=media.mime_type,
            size_bytes=media.size_bytes,
            checksum_sha256=media.checksum_sha256,
        )
        self.session.add(model)
        return MediaDTO(
            original_name=model.original_name,
            storage_key=model.storage_key,
            mime_type=model.mime_type,
            size_bytes=model.size_bytes,
            checksum_sha256=model.checksum_sha256,
            id=model.id,
        )

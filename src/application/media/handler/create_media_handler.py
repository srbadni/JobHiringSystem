import hashlib
import uuid

from domain.attached_resume.models import AttachedResume
from ..dto import MediaDTO
from ...common.ports.unit_of_work import UnitOfWork
from ...media.command.create_media_command import CreateMediaCommand


class CreateMediaHandler:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: CreateMediaCommand) -> MediaDTO:
        async with self.uow:
            sha256 = hashlib.sha256()
            size_bytes = 0

            while chunk := await command.file.read(1024 * 1024):
                size_bytes += len(chunk)
                sha256.update(chunk)

            checksum_sha256 = sha256.hexdigest()

            media_info = MediaDTO(
                original_name=command.file.filename or "",
                storage_key=f"uploads/{uuid.uuid4()}-{command.file.filename}",
                mime_type=command.file.content_type or "",
                size_bytes=size_bytes,
                checksum_sha256=checksum_sha256,
            )

            created_media = await self.uow.media.add(media_info)
            if not created_media.id:
                raise Exception

            await self.uow.attached_resumes.add(AttachedResume(
                media_id=created_media.id,
                applicant_profile_id=command.applicant_profile_id,
            ))

            return created_media

from pathlib import Path
from uuid import uuid4

from domain.attached_resume.models import AttachedResume

from ...common.ports.unit_of_work import UnitOfWork
from ..command.create_media_command import CreateMediaCommand
from ..dto import MediaDTO
from ..ports.file_storage import FileStorage


class CreateMediaHandler:
    def __init__(self, uow: UnitOfWork, file_storage: FileStorage):
        self.uow = uow
        self.file_storage = file_storage

    async def handle(self, command: CreateMediaCommand) -> MediaDTO:
        original_name = Path(command.filename).name
        if not original_name:
            raise ValueError("A file name is required.")

        suffix = Path(original_name).suffix.lower()
        storage_key = f"resumes/{uuid4().hex}{suffix}"
        stored_file = await self.file_storage.save(storage_key, command.file)
        committed = False

        try:
            async with self.uow:
                media_info = MediaDTO(
                    original_name=original_name[:255],
                    storage_key=storage_key,
                    mime_type=(command.content_type or "application/octet-stream")[:127],
                    size_bytes=stored_file.size_bytes,
                    checksum_sha256=stored_file.checksum_sha256,
                )
                created_media = await self.uow.media.add(media_info)
                if created_media.id is None:
                    raise RuntimeError("Media repository did not assign an id.")

                await self.uow.attached_resumes.add(
                    AttachedResume(
                        media_id=created_media.id,
                        applicant_profile_id=command.applicant_profile_id,
                    )
                )
                await self.uow.commit()
                committed = True
                return created_media
        finally:
            if not committed:
                await self.file_storage.delete(storage_key)

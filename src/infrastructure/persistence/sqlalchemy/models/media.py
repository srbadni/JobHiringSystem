"""Database metadata for privately stored files."""

from uuid import UUID

from sqlalchemy import BigInteger, CheckConstraint, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.persistence.sqlalchemy.base import Base


class Media(Base):
    """Metadata for bytes persisted by the configured storage backend."""

    __tablename__ = "media"
    __table_args__ = (
        CheckConstraint("size_bytes > 0", name="ck_media_size_bytes_positive"),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    original_name: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_key: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    mime_type: Mapped[str] = mapped_column(String(127), nullable=False)
    size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    checksum_sha256: Mapped[str] = mapped_column(String(64), nullable=False)

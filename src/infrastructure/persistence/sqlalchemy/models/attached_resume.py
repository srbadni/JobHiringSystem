from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base
if TYPE_CHECKING:
    from ..models.applicant_profile import ApplicantProfile
    from ..models.media import Media


class AttachedResume(Base):
    __tablename__ = "attached_resumes"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    media_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("media.id", ondelete="CASCADE"))
    applicant_profile_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("applicant_profiles.id"))

    applicant_profile: Mapped["ApplicantProfile"] = relationship(
        "ApplicantProfile",
        back_populates="attached_resume",
        init=False,
    )
    media: Mapped["Media"] = relationship(init=False)
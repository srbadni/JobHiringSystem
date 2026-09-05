from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base
if TYPE_CHECKING:
    from ..models.applicant_profile import ApplicantProfile
    from ..models.media import Media


class AttachedResume(Base):
    __tablename__ = "attached_resumes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    media_id: Mapped[int] = mapped_column(Integer, ForeignKey("media.id", ondelete="CASCADE"))
    applicant_profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("applicant_profiles.id"))

    applicant_profile: Mapped["ApplicantProfile"] = relationship(
        "ApplicantProfile",
        back_populates="attached_resume",
        init=False,
    )
    media: Mapped["Media"] = relationship(init=False)
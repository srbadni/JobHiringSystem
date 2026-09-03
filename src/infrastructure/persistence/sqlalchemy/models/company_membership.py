from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .company import Company
    from .user import User


class CompanyMembership(Base):
    """Represents a user's membership in a company."""

    __tablename__ = "company_memberships"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        init=False,
    )

    user_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    company_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("companies.id", ondelete="CASCADE",),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="company_membership",
        init=False,
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="company_memberships",
        init=False,
    )

    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

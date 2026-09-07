"""prevent duplicate job applications

Revision ID: 7f2c0b3f4a1d
Revises: bc7aae6b174b
Create Date: 2026-09-07
"""
from typing import Sequence, Union

from alembic import op


revision: str = "7f2c0b3f4a1d"
down_revision: Union[str, Sequence[str], None] = "bc7aae6b174b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        "uq_job_applications_applicant_job_posting",
        "job_applications",
        ["applicant_id", "job_posting_id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_job_applications_applicant_job_posting",
        "job_applications",
        type_="unique",
    )

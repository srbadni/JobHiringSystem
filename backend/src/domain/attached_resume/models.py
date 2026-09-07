from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class AttachedResume:
    media_id: UUID
    applicant_profile_id: UUID
    id: UUID = field(default_factory=uuid4)

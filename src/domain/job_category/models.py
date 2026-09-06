from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class JobCategory:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)

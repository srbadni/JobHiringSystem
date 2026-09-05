from dataclasses import dataclass


@dataclass
class AttachedResume:
    media_id: int
    applicant_profile_id: int
    id: int | None = None

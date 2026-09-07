class JobApplicationNotFoundError(Exception):
    """Raised when an application or its company/job target does not exist."""


class DuplicateJobApplicationError(Exception):
    """Raised when an applicant has already applied to a job posting."""

from fastapi import UploadFile


class CreateMediaCommand:
    file: UploadFile
    applicant_profile_id: int
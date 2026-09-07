from application.common.ports.unit_of_work import UnitOfWork
from domain.job_posting.models import JobPosting

from ..command.update_job_posting import UpdateJobPostingCommand


class UpdateJobPostingHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: UpdateJobPostingCommand) -> JobPosting:
        async with self.uow:
            current = await self.uow.job_postings.get_by_id(command.job_posting_id)
            job_posting = JobPosting(
                id=command.job_posting_id,
                company_id=command.company_id,
                job_category_id=command.job_category_id,
                province_id=command.province_id,
                city_id=command.city_id,
                salary_range_id=command.salary_range_id,
                job_title=command.job_title,
                job_description=command.job_description,
                company_overview=command.company_overview,
                is_latin_text=command.is_latin_text,
                post_notifications=current.post_notifications,
                employment_type=command.employment_type,
                work_mode=command.work_mode,
                status=command.status,
                work_experience=command.work_experience,
                minimum_education=command.minimum_education,
                gender=command.gender,
                military_status=command.military_status,
            )
            result = await self.uow.job_postings.update(job_posting)
            await self.uow.commit()
            return result

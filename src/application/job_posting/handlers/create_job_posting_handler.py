from domain.job_posting.models import JobPosting
from application.common.ports.unit_of_work import UnitOfWork
from ..command.create_job_posting import CreateJobPostingCommand


class CreateJobPostingHandler:

    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, command: CreateJobPostingCommand) -> JobPosting:
        async with self.uow:
            job_posting_domain_model = JobPosting(
                company_id=command.company_id,
                job_category_id=command.job_category_id,
                province_id=command.province_id,
                city_id=command.city_id,
                salary_range_id=command.salary_range_id,
                job_title=command.job_title,
                job_description=command.job_description,
                company_overview=command.company_overview,
                is_latin_text=command.is_latin_text,
                employment_type=command.employment_type,
                work_mode=command.work_mode,
                status=command.status,
                work_experience=command.work_experience,
                minimum_education=command.minimum_education,
                gender=command.gender,
                military_status=command.military_status,
                post_notifications=False,
            )

            result = await self.uow.job_postings.add(job_posting_domain_model)
            await self.uow.commit()
            return result

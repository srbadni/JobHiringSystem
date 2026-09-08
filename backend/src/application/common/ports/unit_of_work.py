from abc import ABC, abstractmethod

from application.jobs_search.ports.jobs_search_repository import JobsSearchRepository
from application.applicant_profile.ports.applicant_profiles_repository import ApplicantProfilesRepository
from application.applicant_profile.ports.attached_resumes_repository import AttachedResumesRepository
from application.company_activities.ports.company_activity_repository import CompanyActivityRepository
from application.job_categories.ports.job_category_repository import JobCategoryRepository
from application.job_applications.ports.job_application_repository import JobApplicationRepository
from application.locations.ports.location_repository import LocationRepository
from application.salary_ranges.ports.salary_range_repository import SalaryRangeRepository


from ...companies.ports.repositories.company_repository import CompanyRepository
from ...company_membership.ports.company_membership_repository import CompanyMembershipRepository
from ...job_management.ports.job_posting_respository import JobPostingRepository
from ...media.ports.media_repository import MediaRepository

from ...users.ports.users_repository import UsersRepository

from types import TracebackType


class UnitOfWork(ABC):
    users: UsersRepository
    companies: CompanyRepository
    company_memberships: CompanyMembershipRepository
    job_postings: JobPostingRepository
    job_applications: JobApplicationRepository
    jobs_search: JobsSearchRepository
    media: MediaRepository
    attached_resumes: AttachedResumesRepository
    applicant_profiles: ApplicantProfilesRepository
    company_activities: CompanyActivityRepository
    job_categories: JobCategoryRepository
    salary_ranges: SalaryRangeRepository
    locations: LocationRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

from fastapi import FastAPI

from bootstrap.company_activities_providers import (
    provide_create_company_activity_handler,
    provide_delete_company_activity_handler,
    provide_get_company_activity_by_id_handler,
    provide_list_company_activities_handler,
    provide_update_company_activity_handler,
)
from bootstrap.job_categories_providers import (
    provide_create_job_category_handler,
    provide_delete_job_category_handler,
    provide_get_job_category_by_id_handler,
    provide_list_job_categories_handler,
    provide_update_job_category_handler,
)
from bootstrap.salary_ranges_providers import (
    provide_create_salary_range_handler,
    provide_delete_salary_range_handler,
    provide_get_salary_range_by_id_handler,
    provide_list_salary_ranges_handler,
    provide_update_salary_range_handler,
)
from bootstrap.employer_registration_providers import (
    provide_create_employer_and_company_handler,
)
from bootstrap.job_postings_providers import (
    provide_create_job_posting_handler,
    provide_delete_job_posting_handler,
    provide_get_job_posting_by_id_handler,
    provide_list_job_postings_handler,
    provide_update_job_posting_handler,
)
from bootstrap.users_providers import (
    provide_create_user_handler,
    provide_get_all_users_handler,
    provide_get_user_by_email_handler,
    provide_get_user_by_id_handler,
)
from bootstrap.jobs_result_providers import (
    provide_jobs_result_handler,
    provide_company_jobs_result_handler,
    provide_company_details_handler,
    provide_job_details_handler,
)
from bootstrap.media_providers import provide_create_media_handler
from bootstrap.job_applications_providers import (
    provide_create_job_application_handler,
    provide_get_job_application_handler,
    provide_list_my_job_applications_handler,
)
from bootstrap.applicant_profile_providers import (
    provide_educations_handler, provide_job_preference_handler,
    provide_language_skills_handler, provide_skills_handler,
    provide_work_experiences_handler,
)
from presentation.http.api.v1.routers.company_activities.router import create_company_activities_router
from presentation.http.api.v1.routers.job_categories.router import create_job_categories_router
from presentation.http.api.v1.routers.salary_ranges.router import create_salary_ranges_router
from presentation.http.api.v1.routers.users.router import (
    create_users_router,
)
from presentation.http.api.v1.routers.employer.router import create_employer_router
from presentation.http.api.v1.routers.job_postings.router import create_job_postings_router
from presentation.http.api.v1.routers.jobs_result.router import create_jobs_result_router
from presentation.http.api.v1.routers.resume_upload.router import create_resume_upload_router
from presentation.http.api.v1.routers.applicant_profile.router import create_applicant_profile_router
from presentation.http.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(title="Job Hiring System")
    register_exception_handlers(app)

    company_activities_router = create_company_activities_router(
        provide_create_handler=provide_create_company_activity_handler,
        provide_list_handler=provide_list_company_activities_handler,
        provide_get_by_id_handler=provide_get_company_activity_by_id_handler,
        provide_update_handler=provide_update_company_activity_handler,
        provide_delete_handler=provide_delete_company_activity_handler,
    )

    job_categories_router = create_job_categories_router(
        provide_create_handler=provide_create_job_category_handler,
        provide_list_handler=provide_list_job_categories_handler,
        provide_get_by_id_handler=provide_get_job_category_by_id_handler,
        provide_update_handler=provide_update_job_category_handler,
        provide_delete_handler=provide_delete_job_category_handler,
    )

    salary_ranges_router = create_salary_ranges_router(
        provide_create_handler=provide_create_salary_range_handler,
        provide_list_handler=provide_list_salary_ranges_handler,
        provide_get_by_id_handler=provide_get_salary_range_by_id_handler,
        provide_update_handler=provide_update_salary_range_handler,
        provide_delete_handler=provide_delete_salary_range_handler,
    )

    users_router = create_users_router(
        provide_create_user_handler=provide_create_user_handler,
        provide_get_all_users_handler=provide_get_all_users_handler,
        provide_get_user_by_id_handler=provide_get_user_by_id_handler,
        provide_get_user_by_email_handler=provide_get_user_by_email_handler,
    )

    employer_router = create_employer_router(
        provide_create_employer_and_company_handler=provide_create_employer_and_company_handler,
    )

    job_postings_router = create_job_postings_router(
        provide_create_job_posting_handler=provide_create_job_posting_handler,
        provide_list_job_postings_handler=provide_list_job_postings_handler,
        provide_get_job_posting_by_id_handler=provide_get_job_posting_by_id_handler,
        provide_update_job_posting_handler=provide_update_job_posting_handler,
        provide_delete_job_posting_handler=provide_delete_job_posting_handler,
    )

    jobs_result_router = create_jobs_result_router(
        provide_jobs_result_handler=provide_jobs_result_handler,
        provide_company_jobs_result_handler=provide_company_jobs_result_handler,
        provide_company_details_handler=provide_company_details_handler,
        provide_job_details_handler=provide_job_details_handler,
        provide_create_job_application_handler=provide_create_job_application_handler,
        provide_list_my_job_applications_handler=provide_list_my_job_applications_handler,
        provide_get_job_application_handler=provide_get_job_application_handler,
    )

    resume_upload_router = create_resume_upload_router(
        provide_create_media_handler=provide_create_media_handler,
    )

    applicant_profile_router = create_applicant_profile_router(
        provide_skills_handler=provide_skills_handler,
        provide_work_experiences_handler=provide_work_experiences_handler,
        provide_educations_handler=provide_educations_handler,
        provide_language_skills_handler=provide_language_skills_handler,
        provide_job_preference_handler=provide_job_preference_handler,
    )

    app.include_router(
        company_activities_router,
        prefix="/api/v1/company-activities",
    )

    app.include_router(
        job_categories_router,
        prefix="/api/v1/job-categories",
    )

    app.include_router(
        salary_ranges_router,
        prefix="/api/v1/salary-ranges",
    )

    app.include_router(
        users_router,
        prefix="/api/v1/users",
    )

    app.include_router(
        employer_router,
        prefix="/api/v1/employers",
    )

    app.include_router(
        job_postings_router,
        prefix="/api/v1/job_postings",
    )

    app.include_router(
        jobs_result_router,
        prefix="/api/v1/jobs_result",
    )

    app.include_router(
        resume_upload_router,
        prefix="/api/v1/resume-upload",
    )

    app.include_router(
        applicant_profile_router,
        prefix="/api/v1/applicant-profiles",
    )

    return app

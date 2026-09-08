from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    provide_update_user_handler,
    provide_delete_user_handler,
)
from bootstrap.jobs_result_providers import (
    provide_jobs_result_handler,
    provide_company_jobs_result_handler,
    provide_company_details_handler,
    provide_job_details_handler,
)
from bootstrap.media_providers import provide_create_media_handler
from bootstrap.locations_providers import (
    provide_list_cities_handler,
    provide_list_provinces_handler,
)
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
from presentation.http.api.v1.routers.admin.company_activities import create_company_activities_router
from presentation.http.api.v1.routers.admin.job_categories import create_job_categories_router
from presentation.http.api.v1.routers.admin.salary_ranges import create_salary_ranges_router
from presentation.http.api.v1.routers.admin.users import (
    create_users_router,
)
from presentation.http.api.v1.routers.company.job_postings import create_job_postings_router
from presentation.http.api.v1.routers.auth.router import create_auth_router
from presentation.http.api.v1.routers.applicant.jobs import create_jobs_router
from presentation.http.api.v1.routers.applicant.companies import create_companies_router
from presentation.http.api.v1.routers.applicant.applications import create_applications_router
from presentation.http.api.v1.routers.resume_upload.router import create_resume_upload_router
from presentation.http.api.v1.routers.applicant_profile.router import create_applicant_profile_router
from presentation.http.api.v1.routers.locations.router import create_locations_router
from presentation.http.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(title="Job Hiring System")
    register_exception_handlers(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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
        provide_update_user_handler=provide_update_user_handler,
        provide_delete_user_handler=provide_delete_user_handler,
        provide_create_employer_handler=provide_create_employer_and_company_handler,
    )

    auth_router = create_auth_router(
        provide_create_user_handler=provide_create_user_handler,
        provide_create_employer_handler=provide_create_employer_and_company_handler,
    )

    job_postings_router = create_job_postings_router(
        provide_create_job_posting_handler=provide_create_job_posting_handler,
        provide_list_job_postings_handler=provide_list_job_postings_handler,
        provide_get_job_posting_by_id_handler=provide_get_job_posting_by_id_handler,
        provide_update_job_posting_handler=provide_update_job_posting_handler,
        provide_delete_job_posting_handler=provide_delete_job_posting_handler,
    )

    jobs_router = create_jobs_router(provide_jobs_result_handler)
    companies_router = create_companies_router(provide_company_details_handler, provide_company_jobs_result_handler, provide_job_details_handler)
    applications_router = create_applications_router(provide_create_job_application_handler, provide_list_my_job_applications_handler, provide_get_job_application_handler)

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

    locations_router = create_locations_router(
        provide_list_provinces_handler=provide_list_provinces_handler,
        provide_list_cities_handler=provide_list_cities_handler,
    )

    app.include_router(locations_router, prefix="/api/v1")

    app.include_router(
        company_activities_router,
        prefix="/api/v1/admin/company-activities",
    )

    app.include_router(
        job_categories_router,
        prefix="/api/v1/job-categories",
    )

    app.include_router(
        salary_ranges_router,
        prefix="/api/v1/admin/salary-ranges",
    )

    app.include_router(
        users_router,
        prefix="/api/v1/admin/users",
    )

    app.include_router(
        auth_router,
        prefix="/api/v1/auth",
    )

    app.include_router(
        job_postings_router,
        prefix="/api/v1/company/job-postings",
    )

    app.include_router(
        jobs_router,
        prefix="/api/v1/applicant/jobs",
    )
    app.include_router(companies_router, prefix="/api/v1/applicant/companies")
    app.include_router(applications_router, prefix="/api/v1/applicant")

    app.include_router(
        resume_upload_router,
        prefix="/api/v1/resume-upload",
    )

    app.include_router(
        applicant_profile_router,
        prefix="/api/v1/applicant-profiles",
    )

    return app

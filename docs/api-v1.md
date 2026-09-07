# API v1 routing and development identity

All routes are rooted at `/api/v1`. The routing migration is:

| Previous route | Current route |
| --- | --- |
| `/users` | `/admin/users` |
| `/company-activities` | `/admin/company-activities` |
| `/job-categories` | `/admin/job-categories` |
| `/salary-ranges` | `/admin/salary-ranges` |
| `/employers/register` | `/auth/register/employer` |
| user creation used for registration | `/auth/register/applicant` |
| `/job_postings` | `/company/job-postings` |
| `/jobs_result` | `/applicant/jobs/search` |
| `/jobs_result/companies/{company_name}` | `/applicant/companies/{company_name}` |
| `/jobs_result/companies/{company_name}/jobs` | `/applicant/companies/{company_name}/jobs` |
| `/jobs_result/companies/{company_name}/jobs/{job_id}` | `/applicant/companies/{company_name}/jobs/{job_id}` |
| `/jobs_result/companies/{company_name}/jobs/{job_id}/applications` | `/applicant/jobs/{job_id}/applications` |
| `/jobs_result/applications/me` | `/applicant/applications` |
| `/jobs_result/applications/{application_id}` | `/applicant/applications/{application_id}` |

Resume upload and applicant-profile component routes retain their existing paths.

## Temporary development identity

Until authentication is connected, company posting operations require `X-Company-Id`
and applicant application operations require `X-Applicant-Id`. Both values are UUIDs
and are supplied through replaceable FastAPI dependencies. They scope reads and
writes for development, but **are not authentication or real access control**. They
must be replaced by trusted identity claims before production use. Login and JWT
routes are intentionally outside the current API contract.

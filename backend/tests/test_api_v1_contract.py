import os
import unittest
from uuid import UUID
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://test:test@localhost/test")
from bootstrap.app_factory import create_app

class ApiContractTests(unittest.TestCase):
    def test_required_routes_and_methods(self):
        paths = create_app().openapi()["paths"]
        expected = {
            "/api/v1/auth/register/applicant": {"post"},
            "/api/v1/auth/register/employer": {"post"},
            "/api/v1/admin/users": {"get", "post"},
            "/api/v1/admin/users/{user_id}": {"get", "put", "delete"},
            "/api/v1/company/job-postings": {"get", "post"},
            "/api/v1/company/job-postings/{job_posting_id}": {"get", "put", "delete"},
            "/api/v1/applicant/jobs/search": {"get"},
            "/api/v1/applicant/jobs/{job_id}/applications": {"post"},
            "/api/v1/applicant/applications": {"get"},
            "/api/v1/applicant/applications/{application_id}": {"get"},
        }
        for path, methods in expected.items():
            self.assertEqual(methods, set(paths[path]))

    def test_temporary_identity_is_header_not_body(self):
        schema = create_app().openapi()
        operation = schema["paths"]["/api/v1/applicant/jobs/{job_id}/applications"]["post"]
        headers = {parameter["name"] for parameter in operation["parameters"] if parameter["in"] == "header"}
        self.assertIn("X-Applicant-Id", headers)
        create_schema = schema["components"]["schemas"]["JobApplicationCreate"]
        self.assertNotIn("applicant_id", create_schema.get("properties", {}))

    def test_uuid_contract(self):
        user_id = create_app().openapi()["components"]["schemas"]["UserRead"]["properties"]["id"]
        self.assertEqual("uuid", user_id["format"])
        self.assertIs(UUID, UUID)

if __name__ == "__main__":
    unittest.main()

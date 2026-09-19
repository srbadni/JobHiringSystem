import unittest
from datetime import datetime, timezone
from uuid import UUID

from application.common.dto.pagination import Pagination
from application.jobs_search.dto.job_search_result import JobResults, SearchJob
from application.jobs_search.handlers.get_jobs_query_handler import GetJobsQueryHandler
from application.jobs_search.query.get_jobs import GetJobsQuery, SortType
from domain.job_posting.enum import EmploymentType, WorkMode


class FakeCache:
    def __init__(self):
        self.values = {}
        self.set_calls = []

    async def get(self, key):
        return self.values.get(key)

    async def set(self, key, value, *, ttl_seconds):
        self.values[key] = value
        self.set_calls.append((key, value, ttl_seconds))

    async def delete(self, key):
        self.values.pop(key, None)


class FakeJobsSearchRepository:
    def __init__(self, result):
        self.result = result
        self.calls = 0

    async def get_jobs(self, queries):
        self.calls += 1
        return self.result


class FakeUnitOfWork:
    def __init__(self, repository):
        self.jobs_search = repository
        self.entries = 0

    async def __aenter__(self):
        self.entries += 1
        return self

    async def __aexit__(self, *args):
        return None


class JobsSearchCacheTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.result = JobResults(
            jobs=[SearchJob(
                id=UUID("11111111-1111-1111-1111-111111111111"),
                company_id=UUID("22222222-2222-2222-2222-222222222222"),
                company_title="شرکت نمونه",
                company_english_title="Example",
                company_logo=None,
                job_category_title="Engineering",
                province_title="Tehran",
                city_title="Tehran",
                salary_title="Negotiable",
                employment_type=EmploymentType.FULL_TIME,
                work_mode=WorkMode.REMOTE,
                job_title="Backend Developer",
                created_at=datetime(2026, 9, 19, tzinfo=timezone.utc),
            )],
            pagination=Pagination(total=1, page_index=1, page_size=20),
            facets={"remote": 1},
        )
        self.query = GetJobsQuery(
            page_size=20,
            page_index=1,
            sort_type=SortType.MOST_RECENT,
        )

    async def test_cache_miss_queries_repository_and_populates_cache(self):
        cache = FakeCache()
        repository = FakeJobsSearchRepository(self.result)
        handler = GetJobsQueryHandler(FakeUnitOfWork(repository), cache, 120)

        actual = await handler.handle(self.query)

        self.assertEqual(self.result, actual)
        self.assertEqual(1, repository.calls)
        self.assertEqual(120, cache.set_calls[0][2])

    async def test_cache_hit_returns_deserialized_result_without_database_access(self):
        cache = FakeCache()
        repository = FakeJobsSearchRepository(self.result)
        handler = GetJobsQueryHandler(FakeUnitOfWork(repository), cache, 120)
        await handler.handle(self.query)

        actual = await handler.handle(self.query)

        self.assertEqual(self.result, actual)
        self.assertEqual(1, repository.calls)

    def test_equivalent_filter_orders_generate_the_same_key(self):
        first = GetJobsQuery(
            page_size=20,
            page_index=1,
            sort_type=SortType.MOST_RECENT,
            province_ids=[UUID(int=2), UUID(int=1)],
        )
        second = GetJobsQuery(
            page_size=20,
            page_index=1,
            sort_type=SortType.MOST_RECENT,
            province_ids=[UUID(int=1), UUID(int=2)],
        )

        self.assertEqual(
            GetJobsQueryHandler._cache_key(first),
            GetJobsQueryHandler._cache_key(second),
        )


if __name__ == "__main__":
    unittest.main()

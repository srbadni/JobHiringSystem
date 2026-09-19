import unittest

from application.common.dto.pagination import Pagination
from application.jobs_search.decorators.cached_get_jobs_handler import CachedGetJobsHandler
from application.jobs_search.dto.job_search_result import JobResults
from application.jobs_search.query.get_jobs import GetJobsQuery, SortType


class StubGetJobsHandler:
    def __init__(self, result: JobResults) -> None:
        self.result = result
        self.calls = 0

    async def handle(self, query: GetJobsQuery) -> JobResults:
        self.calls += 1
        return self.result


class InMemoryCache:
    def __init__(self) -> None:
        self.values: dict[str, str] = {}
        self.set_calls: list[tuple[str, str, int]] = []

    async def get(self, key: str) -> str | None:
        return self.values.get(key)

    async def set(self, key: str, value: str, *, ttl_seconds: int) -> None:
        self.values[key] = value
        self.set_calls.append((key, value, ttl_seconds))

    async def delete(self, key: str) -> None:
        self.values.pop(key, None)


class CachedGetJobsHandlerTests(unittest.IsolatedAsyncioTestCase):
    async def test_cache_miss_delegates_and_stores_result(self) -> None:
        expected = JobResults(
            jobs=[],
            pagination=Pagination(total=0, page_index=1, page_size=20),
            facets={"province": []},
        )
        decorated = StubGetJobsHandler(expected)
        cache = InMemoryCache()
        handler = CachedGetJobsHandler(decorated, cache, cache_ttl_seconds=300)

        result = await handler.handle(self._query())

        self.assertIs(expected, result)
        self.assertEqual(1, decorated.calls)
        self.assertEqual(1, len(cache.set_calls))
        self.assertEqual(300, cache.set_calls[0][2])

    async def test_cache_hit_does_not_invoke_decorated_handler(self) -> None:
        expected = JobResults(
            jobs=[],
            pagination=Pagination(total=7, page_index=1, page_size=20),
            facets=None,
        )
        cache = InMemoryCache()
        first_handler = CachedGetJobsHandler(
            StubGetJobsHandler(expected), cache, cache_ttl_seconds=300
        )
        await first_handler.handle(self._query())
        decorated = StubGetJobsHandler(expected)

        result = await CachedGetJobsHandler(
            decorated, cache, cache_ttl_seconds=300
        ).handle(self._query())

        self.assertEqual(expected, result)
        self.assertEqual(0, decorated.calls)

    @staticmethod
    def _query() -> GetJobsQuery:
        return GetJobsQuery(
            page_size=20,
            page_index=1,
            sort_type=SortType.MOST_RECENT,
            keywords="python",
        )


if __name__ == "__main__":
    unittest.main()

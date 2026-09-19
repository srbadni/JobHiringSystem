import hashlib
import json
from datetime import datetime
from typing import Any, cast
from uuid import UUID

from application.common.dto.pagination import Pagination
from application.common.ports.cache import CachePort
from application.jobs_search.dto.job_search_result import JobResults, SearchJob
from application.jobs_search.ports.get_jobs_handler import GetJobsHandler
from application.jobs_search.query.get_jobs import GetJobsQuery
from domain.job_posting.enum import EmploymentType, WorkMode


_CACHE_KEY_PREFIX = "applicant:jobs:search:v1"


class CachedGetJobsHandler:
    """Adds read-through caching without coupling the use-case handler to a cache."""

    def __init__(
        self,
        decorated: GetJobsHandler,
        cache: CachePort,
        cache_ttl_seconds: int,
    ) -> None:
        self.decorated = decorated
        self.cache = cache
        self.cache_ttl_seconds = cache_ttl_seconds

    async def handle(self, query: GetJobsQuery) -> JobResults:
        cache_key = self._cache_key(query)
        cached_value = await self.cache.get(cache_key)
        if cached_value is not None:
            return self._deserialize(cached_value)

        result = await self.decorated.handle(query)
        await self.cache.set(
            cache_key,
            self._serialize(result),
            ttl_seconds=self.cache_ttl_seconds,
        )
        return result

    @staticmethod
    def _cache_key(query: GetJobsQuery) -> str:
        payload: dict[str, object] = {
            "keywords": query.keywords,
            "province_ids": sorted(str(value) for value in query.province_ids or []),
            "job_category_ids": sorted(str(value) for value in query.job_category_ids or []),
            "work_modes": sorted(value.value for value in query.work_modes or []),
            "work_experiences": sorted(value.value for value in query.work_experiences or []),
            "salary_range_ids": sorted(str(value) for value in query.salary_range_ids or []),
            "page_size": query.page_size,
            "page_index": query.page_index,
            "sort_type": query.sort_type.value if query.sort_type else None,
        }
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(canonical.encode()).hexdigest()
        return f"{_CACHE_KEY_PREFIX}:{digest}"

    @staticmethod
    def _serialize(result: JobResults) -> str:
        payload: dict[str, object] = {
            "jobs": [
                {
                    "id": str(job.id),
                    "company_id": str(job.company_id),
                    "company_title": job.company_title,
                    "company_english_title": job.company_english_title,
                    "company_logo": job.company_logo,
                    "job_category_title": job.job_category_title,
                    "province_title": job.province_title,
                    "city_title": job.city_title,
                    "salary_title": job.salary_title,
                    "employment_type": job.employment_type.value,
                    "work_mode": job.work_mode.value,
                    "job_title": job.job_title,
                    "created_at": job.created_at.isoformat(),
                }
                for job in result.jobs
            ],
            "pagination": {
                "total": result.pagination.total,
                "page_index": result.pagination.page_index,
                "page_size": result.pagination.page_size,
            },
            "facets": result.facets,
        }
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
    def _deserialize(value: bytes | str) -> JobResults:
        raw_value = value.decode() if isinstance(value, bytes) else value
        payload = cast(dict[str, Any], json.loads(raw_value))
        pagination = cast(dict[str, Any], payload["pagination"])
        jobs = cast(list[dict[str, Any]], payload["jobs"])
        return JobResults(
            jobs=[
                SearchJob(
                    id=UUID(job["id"]),
                    company_id=UUID(job["company_id"]),
                    company_title=job["company_title"],
                    company_english_title=job["company_english_title"],
                    company_logo=job["company_logo"],
                    job_category_title=job["job_category_title"],
                    province_title=job["province_title"],
                    city_title=job["city_title"],
                    salary_title=job["salary_title"],
                    employment_type=EmploymentType(job["employment_type"]),
                    work_mode=WorkMode(job["work_mode"]),
                    job_title=job["job_title"],
                    created_at=datetime.fromisoformat(job["created_at"]),
                )
                for job in jobs
            ],
            pagination=Pagination(
                total=pagination["total"],
                page_index=pagination["page_index"],
                page_size=pagination["page_size"],
            ),
            facets=cast(dict[str, Any] | None, payload.get("facets")),
        )

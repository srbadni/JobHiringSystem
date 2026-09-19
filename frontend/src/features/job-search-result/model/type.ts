import {JobItem} from "@/entities/job-item/model/job-item";
import {Pagination} from "@/shared/api/type";

export enum SortType {
    RELEVANCE = "relevance",
    MOST_RECENT = "most_recent",
    SALARY_DESC = "salary_desc",
}

export const SortTypeLabels = {
    "relevance": "مرتبط ترین",
    "most_recent": "جدیدترین",
    "salary_desc": "بیشترین حقوق",
}

export type JobSearchResultResponse = {
    jobs: JobItem[],
    pagination: Pagination,
    facets: Record<string, any> | undefined
}

import {JobItem, JobQueries} from "@/entities/job-item/model/job-item";
import { httpClient } from "@/shared/api";
import {PaginatedResponse} from "@/shared/api/type";

const PAGE_SIZE = 2;

export const getJobs = async (pageParam: number | undefined, queries: JobQueries): Promise<PaginatedResponse<JobItem>> => {
    const result = await httpClient.get("/applicant/jobs/search", {
        params: {
            page_size: PAGE_SIZE,
            page_index: pageParam,
            province_ids: queries.province_ids,
            job_category_ids: queries.job_category_ids,
            keywords: queries.keywords,
        },
        paramsSerializer: {
            indexes: null
        }
    });
    return result.data
}

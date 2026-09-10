import {JobItem} from "@/entities/job-item/model/job-item";
import { httpClient } from "@/shared/api";

export const getJobs = async (): Promise<JobItem[]> => {
    const result = await httpClient.get("/applicant/jobs/search");
    return result.data
}

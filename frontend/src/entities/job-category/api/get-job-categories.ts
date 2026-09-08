import { get } from "@/shared/api";
import type { JobCategory } from "../model/types";

export async function getJobCategories(signal?: AbortSignal): Promise<JobCategory[]> {
    return get<JobCategory[]>("/job-categories", { signal });
}

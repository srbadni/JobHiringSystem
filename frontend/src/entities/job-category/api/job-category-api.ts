import { cache } from "react";
import type { AxiosInstance } from "axios";
import { httpClient } from "@/shared/api";
import type { JobCategory } from "../model/types";

export function createJobCategoryApi(client: AxiosInstance) {
  return {
    getAll: cache(async (signal?: AbortSignal): Promise<JobCategory[]> => {
      const { data } = await client.get<JobCategory[]>("/job-categories", {
        signal,
      });

      return data;
    }),
  };
}

export const jobCategoryApi = createJobCategoryApi(httpClient);

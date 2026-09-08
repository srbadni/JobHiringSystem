import { queryOptions } from "@tanstack/react-query";
import { jobCategoryApi } from "./job-category-api";

export const jobCategoryKeys = {
  all: ["job-categories"] as const,
};

export const jobCategoryQueries = {
  all: () => queryOptions({
    queryKey: jobCategoryKeys.all,
    queryFn: ({ signal }) => jobCategoryApi.getAll(signal),
    staleTime: 5 * 60 * 1000,
  }),
};

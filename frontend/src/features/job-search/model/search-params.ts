export interface JobSearchValues {
  keywords: string;
  provinceId: string;
  jobCategoryId: string;
}

export type JobSearchParams = Record<string, string | string[] | undefined>;
export const emptyJobSearch: JobSearchValues = { keywords: "", provinceId: "", jobCategoryId: "" };

function first(value: string | string[] | undefined): string {
  return (Array.isArray(value) ? value[0] : value)?.trim() ?? "";
}

export function parseJobSearchParams(params: JobSearchParams): JobSearchValues {
  return {
    keywords: first(params.keywords),
    provinceId: first(params.province_id),
    jobCategoryId: first(params.job_category_id),
  };
}

export function buildJobSearchHref(values: JobSearchValues): string {
  const params = new URLSearchParams();
  if (values.keywords.trim()) params.set("keywords", values.keywords.trim());
  if (values.provinceId.trim()) params.set("province_id", values.provinceId.trim());
  if (values.jobCategoryId.trim()) params.set("job_category_id", values.jobCategoryId.trim());
  const query = params.toString();
  return query ? `/jobs/search?${query}` : "/jobs/search";
}

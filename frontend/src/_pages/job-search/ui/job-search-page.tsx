import type { Metadata } from "next";
import { JobSearchForm, buildJobSearchHref, parseJobSearchParams, type JobSearchParams } from "@/features/job-search";
import { Typography } from "@/shared/ui/typography";
import BreadCrumb from "@/shared/ui/bread-crumb/ui/bread-crumb";

export const metadata: Metadata = { title: "جستجوی شغل | سامانه استخدام" };

export async function JobSearchPage({ searchParams }: { searchParams: Promise<JobSearchParams> }) {
  const values = parseJobSearchParams(await searchParams);
  return (
    <main className="px-3 py-4">
      <BreadCrumb steps={[{title: "صفحه اصلی"}, {title: "فرصت های شغلی"}]} />
      <JobSearchForm key={buildJobSearchHref(values)} initialValues={values} className="mt-3" />
      {/* No jobs endpoint or response contract was included in the source project. */}
      <Typography tone="muted" className="mt-5">
        فهرست فرصت‌های شغلی به‌زودی در دسترس قرار می‌گیرد.
      </Typography>
    </main>
  );
}

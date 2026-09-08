import {Typography} from "@/features/widgets/typography";
import JobSearchBar from "@/features/job-search/components/job-search-bar/job-search-bar";

export default function Home() {
  return <main>
    <section className="px-3 py-4">
      <div className="flex flex-col gap-3">
        <Typography variant="h1">
          شغلی که میخوای،
        </Typography>
        <Typography variant="h1" tone="primary">
          آینده ای که می‌سازی
        </Typography>
      </div>
      <Typography tone="muted" className="mt-5">
        فرصت‌های شغلی را کشف کن، شرکت‌ها را بشناس و جایی را پیدا کن که مهارت‌هایت دیده می‌شوند.
      </Typography>
      <JobSearchBar classnames="mt-3" />
    </section>
  </main>;
}

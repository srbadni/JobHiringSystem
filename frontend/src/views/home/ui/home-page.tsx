import { JobSearchForm } from "@/features/job-search";
import { Typography } from "@/shared/ui";

export function HomePage() {
    return <main>
        <section className="px-3 py-4">
            <div className="flex flex-col gap-3">
                <Typography as="h1" variant="h1">شغلی که می‌خوای،</Typography>
                <Typography as="p" variant="h1" tone="primary">آینده‌ای که می‌سازی</Typography>
            </div>
            <Typography tone="muted" className="mt-5">فرصت‌های شغلی را کشف کن، شرکت‌ها را بشناس و جایی را پیدا کن که مهارت‌هایت دیده می‌شوند.</Typography>
            <JobSearchForm className="mt-3" />
        </section>
    </main>;
}

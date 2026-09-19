import type {Metadata} from "next";
import {parseJobSearchParams, type JobSearchParams} from "@/features/job-search-form";
import ResultSearchHero from "@/widgets/result-search-hero/ui/result-search-hero";
import JobSearchResult from "@/features/job-search-result/ui/job-search-result";

export const metadata: Metadata = {title: "جستجوی شغل | سامانه استخدام"};

export async function JobSearchPage({searchParams}: { searchParams: Promise<JobSearchParams> }) {
    const values = parseJobSearchParams(await searchParams);
    return (
        <main className="px-4 py-4">
            <section>
                <ResultSearchHero searchParams={values}/>
            </section>
            <section className="pt-8">
                <JobSearchResult/>
            </section>
        </main>
    );
}

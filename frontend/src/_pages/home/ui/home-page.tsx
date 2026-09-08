import JobCategorySection from "@/widgets/job-categories-selection-section/ui/job-category-section";
import HomeSearchHero from "@/widgets/home-search-hero/home-search-hero";

export function HomePage() {
    return (
        <main>
            <section className="py-4 px-3">
                <HomeSearchHero />
            </section>
            <section className="pt-6">
                <JobCategorySection classnames="px-2"/>
            </section>
        </main>
    );
}

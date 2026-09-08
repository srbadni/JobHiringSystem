import {FC, Fragment} from "react";
import {Typography} from "@/shared/ui/typography";
import {JobSearchForm} from "@/features/job-search";
import Tag from "@/shared/ui/tag/tag";

interface HomeSearchHeroProps {

}

const HomeSearchHero:FC<HomeSearchHeroProps> = ({}) => {
    return (
        <Fragment>
            <Typography as="h1" variant="h1" className="flex flex-col gap-3">
                <span>شغلی که میخوای،</span>
                <span className="text-primary">آینده‌ای که می‌سازی</span>
            </Typography>
            <Typography tone="muted" className="mt-5">
                فرصت‌های شغلی را کشف کن، شرکت‌ها را بشناس و جایی را پیدا کن که مهارت‌هایت دیده می‌شوند.
            </Typography>
            <JobSearchForm className="mt-3"/>
            <div className="flex items-center gap-1 pt-5">
                <Typography tone="muted" variant="caption">
                    جست و جو های محبوب:
                </Typography>
                <div className="flex items-center">
                    <Tag>
                        خوب
                    </Tag>
                </div>
            </div>
        </Fragment>
    );
};

export default HomeSearchHero;

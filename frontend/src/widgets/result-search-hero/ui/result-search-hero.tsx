import {FC, Fragment} from "react";
import BreadCrumb from "@/shared/ui/bread-crumb/ui/bread-crumb";
import {buildJobSearchHref, JobSearchForm, JobSearchValues} from "@/features/job-search-form";

interface ResultSearchHeroProps {
    searchParams: JobSearchValues
}

const ResultSearchHero:FC<ResultSearchHeroProps> = ({searchParams}) => {
    return (
        <Fragment>
            <BreadCrumb steps={[{title: "صفحه اصلی"}, {title: "فرصت های شغلی"}]} />
            <JobSearchForm key={buildJobSearchHref(searchParams)}
                           initialValues={searchParams}
                           className="mt-3" />
        </Fragment>
    );
};

export default ResultSearchHero;

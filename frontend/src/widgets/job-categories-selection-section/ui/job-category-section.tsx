import {FC} from "react";
import {Typography} from "@/shared/ui/typography";
import classNames from "classnames";
import JobCategorySelector from "@/features/select-job-category/ui/JobCategorySelector";

interface JobCategorySectionProps {
    classnames?: string | undefined
}

const JobCategorySection:FC<JobCategorySectionProps> = ({classnames}) => {

    return (
        <div className={classNames("bg-white border border-gray-200 py-6", classnames)}>
            <Typography variant="caption" tone="secondary" className="!font-bold">
                از علاقه ات شروع کن
            </Typography>
            <JobCategorySelector />
        </div>
    );
};

export default JobCategorySection;

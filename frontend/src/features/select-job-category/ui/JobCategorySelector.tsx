import {FC} from "react";
import {Typography} from "@/shared/ui/typography";
import {ArrowLeftIcon} from "@/shared/ui/icons/ArrowLeftIcon";

interface JobCategorySelectorProps {

}

const JobCategorySelector: FC<JobCategorySelectorProps> = ({}) => {
    return (
        <div>
            <div className="flex items-end">
                <div className="w-50">
                    <Typography variant="h2">
                        در چه حوزه ای دنبال کار میگردی؟
                    </Typography>
                </div>
                <div className="w-50 flex justify-end items-center gap-1 h-fit">
                    <Typography variant="caption" className="!font-bold" tone="primary">
                        همه فرصت ها
                    </Typography>
                    <ArrowLeftIcon className="text-primary" width={18} height={18} />
                </div>
            </div>
        </div>
    );
};

export default JobCategorySelector;

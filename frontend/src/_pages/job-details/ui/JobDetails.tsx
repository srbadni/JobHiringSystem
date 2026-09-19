import React, {FC} from 'react';
import BreadCrumb from "@/shared/ui/bread-crumb/ui/bread-crumb";
import BackButton from "@/shared/ui/back-button/BackButton";

interface JobDetailsProps {

}

const JobDetails: FC<JobDetailsProps> = ({}) => {
    return (
        <div>
            <div className="flex justify-between px-4 py-4">
                <BreadCrumb steps={[{title: "صفحه اصلی"}, {title: "فرصت های شغلی"}]} />
                <BackButton title="بازگشت به نتایج" />
            </div>
        </div>
    );
};

export {JobDetails};

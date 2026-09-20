import React, {FC} from 'react';
import BreadCrumb from "@/shared/ui/bread-crumb/ui/bread-crumb";
import BackButton from "@/shared/ui/back-button/BackButton";
import JobCardItemWrapper from "@/entities/job-details/ui/JobCardItemWrapper";
import {Typography} from "@/shared/ui/typography";
import {getJobDetailsQuery} from "@/entities/job-details/api/get-job-details-query";
import {mapJobDetailsToJobItem} from "@/entities/job-item/utils/mapJobDetailsToJobItem";
import {PrimaryButton} from "@/shared/ui/button";
import {createJobApplication} from "@/entities/job-application/actions/actions";

interface JobDetailsProps {
    params: Promise<{
        company_name: string;
        job_id: string;
    }>;
}

const JobDetails: FC<JobDetailsProps> = async ({params}) => {
    const paramsValue = await params;

    const jobsDetails = await getJobDetailsQuery({
        jobId: paramsValue.job_id,
        companyName: paramsValue.company_name,
    })

    return (
        <div className="px-4 py-4">
            <div className="flex justify-between">
                <BreadCrumb steps={[{title: "صفحه اصلی"}, {title: "فرصت های شغلی"}]} />
                <BackButton title="بازگشت به نتایج" />
            </div>
            <div className="flex pt-5">
                <JobCardItemWrapper job={mapJobDetailsToJobItem(jobsDetails)} detailUrl={`/jobs/${paramsValue.company_name}/${paramsValue.job_id}`} />
            </div>
            <div className="flex flex-col gap-3 bg-white mt-5 border border-gray-200 rounded-lg p-3">
                <div>
                    <Typography as="span" className="!font-bold mb-2" tone="primary">شرح موقعیت شغلی</Typography>
                    <Typography as="p" variant="small">
                        {jobsDetails.job_description}
                    </Typography>
                </div>
                <div className="border-b border-gray-200"></div>
                <div>
                    <Typography as="span" className="!font-bold mb-2" tone="primary">معرفی شرکت</Typography>
                    <Typography as="p" variant="small">
                        {jobsDetails.company_overview}
                    </Typography>
                </div>
            </div>
            <div className="fixed bottom-0 left-0 right-0 bg-white p-4 border-t border-gray-200">
                <div className="flex w-full px-4">
                    <div className="flex flex-col">
                        <Typography as="span" variant="caption" tone="muted">حقوق ماهانه</Typography>
                        <Typography as="span" variant="body" className="!font-bold">
                            {jobsDetails.salary_range}
                        </Typography>
                    </div>
                    <form className="ms-auto" action={createJobApplication}>
                        <input
                            type="hidden"
                            name="jobId"
                            value={paramsValue.job_id}
                        />

                        <input
                            type="hidden"
                            name="applicant_id"
                            value="80021f27-9b26-4368-9f16-749c058f1525"
                        />

                        <PrimaryButton type="submit">
                            ارسال رزومه
                        </PrimaryButton>
                    </form>
                </div>
            </div>
        </div>
    );
};

export {JobDetails};

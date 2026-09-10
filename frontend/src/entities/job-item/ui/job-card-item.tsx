"use client"

import {FC} from "react";
import {Typography} from "@/shared/ui/typography";
import {Tag} from "@/shared/ui/tag/tag";
import {BriefcaseIcon} from "@/shared/ui/icons/BriefcaseIcon";
import {LocationIcon} from "@/shared/ui/icons";
import {Button} from "@/shared/ui/button";
import {JobItem} from "@/entities/job-item/model/job-item";

interface JobCardItemProps {
    job: JobItem
}

const JobCardItem:FC<JobCardItemProps> = ({job}) => {
    return (
        <div className="bg-white border border-gray-200 rounded-lg p-3 flex flex-col">
            <div className="flex gap-3 pb-3 border-b border-gray-200">
                <span>logo</span>
                <div className="flex flex-col">
                    <Typography variant="lead" className="!font-bold">{job.job_title}</Typography>
                    {/*<Tag className="w-fit" variant="warning" icon={<BriefcaseIcon width={14} height={14} />}>*/}
                    {/*    آگهی ویژه*/}
                    {/*</Tag>*/}
                    <Typography variant="caption" tone="muted">{job.company_title} | {job.company_english_title}</Typography>
                    <div className="inline-flex gap-3">
                        <span className="inline-flex items-center gap-1">
                            <LocationIcon className="text-muted" width={14} height={14} />
                            <Typography variant="caption" tone="muted">{job.province_title}، {job.city_title}</Typography>
                        </span>
                        <span className="inline-flex items-center gap-1">
                            <BriefcaseIcon className="text-muted" width={14} height={14} />
                            <Typography variant="caption" tone="muted">تست</Typography>
                        </span>
                    </div>
                </div>
            </div>
            <div className="flex justify-between items-center">
                <div className="flex flex-col pt-2">
                    <Typography className="!font-bold" variant="small">
                        {job.salary_range_title}
                    </Typography>
                    <Typography tone="muted" variant="small">
                        3 ساعت پیش
                    </Typography>
                </div>
                <Button className="bg-indigo-50">
                    <Typography className="text-primary !font-bold" variant="small">
                        ارسال رزومه
                    </Typography>
                </Button>
            </div>
        </div>
    );
};

export default JobCardItem;

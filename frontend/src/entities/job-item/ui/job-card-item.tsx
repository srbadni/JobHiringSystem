"use client"

import {FC} from "react";
import {Typography} from "@/shared/ui/typography";
import Image from "next/image";
import {BriefcaseIcon} from "@/shared/ui/icons/BriefcaseIcon";
import {DEFAULT_COMPANY_LOGO, LocationIcon} from "@/shared/ui/icons";
import {Button, PrimaryButton} from "@/shared/ui/button";
import {employmentTypeLabels, JobItem, workModeLabels} from "@/entities/job-item/model/job-item";
import {BookmarkIcon} from "@/shared/ui/icons/BookmarkIcon";
import {timeAgo} from "@/shared/utils/datetime";
import SearchTag from "@/shared/ui/tag/search-tag";

interface JobCardItemProps {
    job: JobItem
}

const JobCardItem:FC<JobCardItemProps> = ({job}) => {
    return (
        <div className="bg-white border border-gray-200 rounded-lg p-3 flex flex-col">
            <div className="pb-3 border-b border-gray-200">
                <div className="flex gap-3 pb-1">
                    <Image src={job.company_logo || DEFAULT_COMPANY_LOGO} className="h-[45px] w-[45px] rounded-lg" alt={job.company_title} width={45} height={45} />
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
                            <Typography variant="caption" tone="muted">{employmentTypeLabels[job.employment_type]}</Typography>
                        </span>
                        </div>
                    </div>
                    <div className="ms-auto">
                        <BookmarkIcon width={18} height={18} className="text-muted" />
                    </div>
                </div>
                <div className="flex gap-2">
                    <SearchTag bgMode="muted">
                        {workModeLabels[job.work_mode]}
                    </SearchTag>
                </div>
            </div>
            <div className="flex justify-between items-center pt-2">
                <div className="flex flex-col pt-2">
                    <Typography className="!font-bold" variant="small">
                        {job.salary_title}
                    </Typography>
                    <Typography tone="muted" variant="small">
                        {timeAgo(job.created_at)}
                    </Typography>
                </div>
                <PrimaryButton>
                    <Typography className="text-white !font-bold" variant="small">
                        ارسال رزومه
                    </Typography>
                </PrimaryButton>
            </div>
        </div>
    );
};

export default JobCardItem;

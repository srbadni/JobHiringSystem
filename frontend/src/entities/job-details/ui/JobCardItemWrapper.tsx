"use client"
import React, {FC} from 'react';
import JobCardItem from "@/entities/job-item/ui/job-card-item";
import {JobItem} from "@/entities/job-item/model/job-item";

interface JobCardItemWrapperProps {
    detailUrl: string,
    job: JobItem
}

const JobCardItemWrapper:FC<JobCardItemWrapperProps> = ({job, detailUrl}) => {

    return (
        <JobCardItem.Root className="w-full" detailUrl={detailUrl} job={job}>
            <JobCardItem.Header>
                <JobCardItem.Overview>
                    <JobCardItem.CompanyLogo />
                    <JobCardItem.Information>
                        <JobCardItem.Title />
                        <JobCardItem.CompanyName />
                        <JobCardItem.JobDetails />
                    </JobCardItem.Information>
                    <JobCardItem.Bookmark />
                </JobCardItem.Overview>
                <JobCardItem.Tags />
            </JobCardItem.Header>
        </JobCardItem.Root>
    );
};

export default JobCardItemWrapper;

"use client"
import {FC} from "react";
import {Typography} from "@/shared/ui/typography";
import {Button} from "@/shared/ui/button";
import {FilterIcon} from "@/shared/ui/icons/FilterIcon";
import JobCardItem from "@/entities/job-item/ui/job-card-item";
import {useQuery} from "@tanstack/react-query";
import {getJobs} from "@/entities/job-item/api/get-jobs-query";

interface JobSearchResultProps {

}

const JobSearchResult:FC<JobSearchResultProps> = ({}) => {

    const {data: jobs = [], isPending} = useQuery({
        queryKey: ["jobs"],
        queryFn: getJobs
    })

    return (
        <div className="flex flex-col gap-1">
            <div className="flex gap-2 items-end border-b border-b-gray-200 pb-5 mb-4">
                <Typography variant="small" className="!font-bold">
                    <span>تست</span>
                </Typography>
                <Button className="flex gap-2 bg-white ms-auto border border-gray-200">
                    <FilterIcon width={16} height={16} />
                    <Typography className="!font-bold" variant="small">فیلتر ها</Typography>
                </Button>
            </div>
            <div className="flex flex-col gap-3">
                {
                    isPending ? <span>loading ...</span> : (
                        jobs.map(j => (
                            <JobCardItem key={j.id} job={j} />
                        ))
                    )
                }
            </div>
        </div>
    );
};

export default JobSearchResult;

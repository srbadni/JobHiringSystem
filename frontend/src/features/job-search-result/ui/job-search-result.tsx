"use client"
import {FC, Fragment} from "react";
import {Typography} from "@/shared/ui/typography";
import {Button} from "@/shared/ui/button";
import {FilterIcon} from "@/shared/ui/icons/FilterIcon";
import JobCardItem from "@/entities/job-item/ui/job-card-item";
import {InfiniteData, useInfiniteQuery, useQuery} from "@tanstack/react-query";
import {getJobs} from "@/entities/job-item/api/get-jobs-query";
import {PaginatedResponse} from "@/shared/api/type";
import {JobItem} from "@/entities/job-item/model/job-item";
import {useSearchParams} from "next/navigation";

interface JobSearchResultProps {

}

const JobSearchResult:FC<JobSearchResultProps> = ({}) => {
    const searchParams = useSearchParams()
    const keywords = searchParams.get("keywords");
    const province_ids = searchParams.get("province_ids")?.split("|") ?? null;
    const job_category_ids = searchParams.get("job_category_ids")?.split("|") ?? null;

    const {data: jobResults, isPending, hasNextPage, fetchNextPage} = useInfiniteQuery<PaginatedResponse<JobItem>, any, InfiniteData<PaginatedResponse<JobItem>>, any, number>({
        queryKey: ["jobs", {
            keywords,
            province_ids,
            job_category_ids,
        }],
        initialPageParam: 1,
        getNextPageParam: (lastPage) => {
            const skippedPages = lastPage.page_size * lastPage.page_index;
            if ((lastPage.total - skippedPages) <= 0) {
                return;
            }
            return lastPage.page_index + 1;
        },
        queryFn: ({pageParam}) => getJobs(pageParam, {
            keywords,
            province_ids,
            job_category_ids,
        })
    })

    const lastPage = jobResults?.pages[jobResults?.pages.length - 1];

    const mergePagesJobs = jobResults?.pages.flatMap(p => (
        p.items
    ))

    return (
        <div className="flex flex-col gap-1">
            <div className="flex gap-2 items-end border-b border-b-gray-200 pb-5 mb-4">
                <Typography variant="small" className="!font-bold">
                    {
                        lastPage && (
                            <span>{lastPage?.total} فرصت شغلی</span>
                        )
                    }
                </Typography>
                <Button className="flex gap-2 bg-white ms-auto border border-gray-200">
                    <FilterIcon width={16} height={16} />
                    <Typography className="!font-bold" variant="small">فیلتر ها</Typography>
                </Button>
            </div>
            <div className="flex flex-col gap-3">
                {
                    isPending ? <span>loading ...</span> : (
                        mergePagesJobs?.map((j, index) => {
                            return <Fragment key={j.id}>
                                <JobCardItem job={j} />
                                {
                                    ((mergePagesJobs?.length  - 1) === index && hasNextPage) && (
                                        <Button onClick={() => fetchNextPage()} className="bg-indigo-50">
                                            <Typography className="text-primary !font-bold" variant="small">
                                                مشاهده بیشتر ...
                                            </Typography>
                                        </Button>
                                    )
                                }
                            </Fragment>
                        })
                    )
                }
            </div>
        </div>
    );
};

export default JobSearchResult;

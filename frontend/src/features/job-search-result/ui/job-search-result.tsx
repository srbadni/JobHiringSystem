"use client"
import {ChangeEvent, FC, Fragment} from "react";
import {Typography} from "@/shared/ui/typography";
import {Button} from "@/shared/ui/button";
import {FilterIcon} from "@/shared/ui/icons/FilterIcon";
import JobCardItem from "@/entities/job-item/ui/job-card-item";
import {InfiniteData, useInfiniteQuery} from "@tanstack/react-query";
import {getJobs} from "@/entities/job-item/api/get-jobs-query";
import {usePathname, useRouter, useSearchParams} from "next/navigation";
import {Select} from "@/shared/ui/select";
import {JobSearchResultResponse, SortType} from "@/features/job-search-result/model/type";
import {JobItem} from "@/entities/job-item/model/job-item";

interface JobSearchResultProps {
    //
}

const JobSearchResult:FC<JobSearchResultProps> = ({}) => {
    const router = useRouter();
    const searchParams = useSearchParams()
    const pathname = usePathname()
    const keywords = searchParams.get("keywords");
    const province_ids = searchParams.get("province_ids")?.split("|") ?? null;
    const job_category_ids = searchParams.get("job_category_ids")?.split("|") ?? null;
    const sort_type = (searchParams.get("sort_type") ?? undefined) as SortType | undefined;

    const {data: jobResults, isPending, hasNextPage, fetchNextPage} = useInfiniteQuery<JobSearchResultResponse, any, InfiniteData<JobSearchResultResponse>, any, number>({
        queryKey: ["jobs", {
            keywords,
            province_ids,
            job_category_ids,
            sort_type,
        }],
        initialPageParam: 1,
        getNextPageParam: (lastPage) => {
            const skippedPages = lastPage.pagination.page_size * lastPage.pagination.page_index;
            if ((lastPage.pagination.total - skippedPages) <= 0) {
                return;
            }
            return lastPage.pagination.page_index + 1;
        },
        queryFn: ({pageParam}) => getJobs(pageParam, {
            keywords,
            province_ids,
            job_category_ids,
            sort_type,
        })
    })

    const lastPage = jobResults?.pages[jobResults?.pages.length - 1];

    const mergePagesJobs = jobResults?.pages.flatMap(p => (
        p.jobs
    ))

    const handleSelect = (event: ChangeEvent<HTMLSelectElement, HTMLSelectElement>) => {
        const params = new URLSearchParams(searchParams.toString())
        if (event.target.value === SortType.RELEVANCE) {
            if (params.has("sort_type")) {
                params.delete("sort_type")
            }
        } else {
            params.set("sort_type", event.target.value)
        }
        router.push(pathname + "?" + params.toString())
    }

    const handleJobClick = (j: JobItem) => {
        router.push(`/jobs/${j.company_english_title}/${j.id}`)
    }

    return (
        <div className="flex flex-col gap-1">
            <div className="flex gap-2 items-end border-b border-b-gray-200 pb-5 mb-4">
                <Typography variant="small" className="!font-bold">
                    {
                        lastPage && (
                            <span>{lastPage?.pagination.total} فرصت شغلی</span>
                        )
                    }
                </Typography>
                <Button className="flex gap-2 bg-white !py-1 ms-auto border border-gray-200">
                    <FilterIcon width={16} height={16} />
                    <Typography className="!font-bold" variant="small">فیلتر ها</Typography>
                </Button>
                <Select value={sort_type ?? SortType.RELEVANCE} onChange={(event) => handleSelect(event)} className="flex gap-2 bg-white !w-fit !py-1 !rounded-md !h-auto border border-gray-200">
                    <option value={SortType.RELEVANCE}>
                        <Typography className="!font-bold" variant="caption">مرتبط‌ترین</Typography>
                    </option>
                    <option value={SortType.MOST_RECENT}>
                        <Typography className="!font-bold" variant="caption">جدیدترین</Typography>
                    </option>
                    <option value={SortType.SALARY_DESC}>
                        <Typography className="!font-bold" variant="caption">بیشترین حقوق</Typography>
                    </option>
                </Select>
            </div>
            <div className="flex flex-col gap-3">
                {
                    isPending ? <span>loading ...</span> : (
                        mergePagesJobs?.map((j, index) => {
                            return <Fragment key={j.id}>
                                <JobCardItem handleClick={handleJobClick} job={j} />
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

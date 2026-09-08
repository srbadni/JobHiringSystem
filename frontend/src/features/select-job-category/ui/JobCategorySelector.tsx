import {Typography} from "@/shared/ui/typography";
import {ArrowLeftIcon} from "@/shared/ui/icons/ArrowLeftIcon";
import JobCategoryThumbCard from "@/entities/job-category/ui/job-category-thumb-card";
import {jobCategoryApi} from "@/entities/job-category";
import Image from "next/image"

interface JobCategorySelectorProps {

}

async function JobCategorySelector(props: JobCategorySelectorProps) {
    const jobCategories = await jobCategoryApi.getAll()
    const slicedJobCategories = jobCategories.slice(0, 6)

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
            <div className="grid grid-cols-2 pt-5 gap-3">
                {
                    slicedJobCategories.map(j => (
                        <JobCategoryThumbCard key={j.id}
                                              url=""
                                              logo={
                                                  <Image
                                                      src={`/icons/job-categories/${j.code}.svg`}
                                                      alt=""
                                                      width={40}
                                                      height={40}
                                                  />
                                              }
                                              title={j.title}
                        />
                    ))
                }
            </div>
        </div>
    );
};

export default JobCategorySelector;

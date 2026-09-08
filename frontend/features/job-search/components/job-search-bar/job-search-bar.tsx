"use client"
import classNames from "classnames";
import {SearchIcon} from "@/features/shared/components/SearchIcon";
import {LocationIcon} from "@/features/shared/components/LocationIcon";
import {CategoryIcon} from "@/features/shared/components/CategoryIcon";
import PrimaryButton from "@/features/shared/components/PrimaryButton";
import ProvinceSelect from "@/entities/location/ui/province-select";
import {useQuery} from "@tanstack/react-query";
import provinceServices from "@/entities/location/service/province.services";
import jobCategoriesServices from "@/entities/job-categories/service/job-categories.services";
import JobCategorySelect from "@/entities/job-categories/ui/JobCategorySelect";
import {useState} from "react";
import {useRouter} from "next/navigation";

interface JobSearchBarProps {
    classnames?: string | undefined
}

function JobSearchBar({classnames}: JobSearchBarProps){
    const router = useRouter()
    const [selectedJobCategoryID, setSelectedJobCategoryID] = useState("")
    const [selectedProvinceID, setSelectedProvinceID] = useState<string>("")
    const [keywords, setKeywords] = useState<string>("")

    const handleKeywordsChange = (value: string) => {
        setKeywords(value)
    }

    const handleSearch = () => {
        router.push(`/jobs/search?keywords=${keywords}&province_id=${selectedProvinceID}&job_category_id=${selectedJobCategoryID}`)
    }

    const {data: provinces = []} = useQuery({
        queryKey: ["provinces"],
        queryFn: provinceServices.get_all,
    })

    const {data: jobCategories = []} = useQuery({
        queryKey: ["job-categories"],
        queryFn: jobCategoriesServices.get_all,
    })

    return (
        <div className={classNames("bg-white rounded-md border border-gray-300 p-2 flex flex-col", classnames)}>
            <div className="flex items-center gap-2 py-1 h-10">
                <SearchIcon width={18} height={18} color="#667085" />
                <input value={keywords}
                       onChange={(event) => handleKeywordsChange(event.target.value)}
                       placeholder="عنوان شغل، مهارت یا شرکت"
                       type="text"
                       className="flex-1 outline-0"/>
            </div>
            <div className="flex items-center gap-2 py-1">
                <LocationIcon width={18} height={18} color="#667085" />
                <ProvinceSelect selectedProvinceID={selectedProvinceID}
                                setSelectedProvinceID={setSelectedProvinceID}
                                provinces={provinces}
                                classnames="border-0" />
            </div>
            <div className="flex items-center gap-2 py-1">
                <CategoryIcon width={18} height={18} color="#667085" />
                <JobCategorySelect selectedJobCategoryID={selectedJobCategoryID}
                                   setSelectedJobCategoryID={setSelectedJobCategoryID}
                                   jobCategories={jobCategories} />
            </div>
            <PrimaryButton onClick={handleSearch} className="bg-primary text-white rounded-md py-2">
                جستجو
            </PrimaryButton>
        </div>
    );
};

export default JobSearchBar;

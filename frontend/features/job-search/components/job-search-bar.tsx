import {FC} from "react";
import classNames from "classnames";
import {SearchIcon} from "@/features/shared/components/SearchIcon";
import {LocationIcon} from "@/features/shared/components/LocationIcon";
import {Select} from "@/features/shared/components/Select";
import {CategoryIcon} from "@/features/shared/components/CategoryIcon";
import PrimaryButton from "@/features/shared/components/PrimaryButton";

interface JobSearchBarProps {
    classnames?: string | undefined
}

const JobSearchBar:FC<JobSearchBarProps> = ({classnames}) => {
    return (
        <div className={classNames("bg-white rounded-md border border-gray-300 p-2 flex flex-col", classnames)}>
            <div className="flex items-center gap-2 py-1 h-10">
                <SearchIcon width={18} height={18} color="#667085" />
                <input placeholder="عنوان شغل، مهارت یا شرکت" type="text" className="flex-1 outline-0"/>
            </div>
            <div className="flex items-center gap-2 py-1">
                <LocationIcon width={18} height={18} color="#667085" />
                <Select className="border-0" defaultValue="">
                    <option value="" disabled>
                        انتخاب شهر
                    </option>

                    <option value="tehran">
                        تهران
                    </option>

                    <option value="isfahan">
                        اصفهان
                    </option>
                </Select>
            </div>
            <div className="flex items-center gap-2 py-1">
                <CategoryIcon width={18} height={18} color="#667085" />
                <Select className="border-0" defaultValue="">
                    <option value="" disabled>
                        انتخاب دسته بندی
                    </option>

                    <option value="web">
                        برنامه نویسی
                    </option>
                </Select>
            </div>
            <PrimaryButton className="bg-primary text-white rounded-md py-2">
                جستجو
            </PrimaryButton>
        </div>
    );
};

export default JobSearchBar;

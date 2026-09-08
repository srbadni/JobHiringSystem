import React, {ChangeEvent, Dispatch, FC, SetStateAction} from 'react';
import {Select} from "@/features/shared/components/Select";
import JobCategories from "@/entities/job-categories/model/type";

interface JobCategorySelectProps {
    jobCategories: JobCategories
    selectedJobCategoryID: string
    setSelectedJobCategoryID: Dispatch<SetStateAction<string>>
}

const JobCategorySelect:FC<JobCategorySelectProps> = ({jobCategories, setSelectedJobCategoryID, selectedJobCategoryID}) => {

    const handleChange = (event: ChangeEvent<HTMLSelectElement, HTMLSelectElement>) => {
        setSelectedJobCategoryID(event.target.value)
    }

    return (
        <Select value={selectedJobCategoryID} onChange={handleChange} className="border-0" defaultValue="">
            <option value="" disabled>
                انتخاب دسته بندی
            </option>

            {
                jobCategories.map(j => (
                    <option key={j.id} value={j.id}>
                        {j.title}
                    </option>
                ))
            }
        </Select>
    );
};

export default JobCategorySelect;

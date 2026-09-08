"use client"

import {ChangeEvent, Dispatch, FC, SetStateAction} from "react";
import {Select} from "@/features/shared/components/Select";
import {Province} from "@/entities/location/model/provinecs";

interface ProvinceSelectProps {
    classnames?: string | undefined
    provinces: Province[]
    selectedProvinceID: string
    setSelectedProvinceID: Dispatch<SetStateAction<string>>
}

const ProvinceSelect:FC<ProvinceSelectProps> = ({classnames, provinces, selectedProvinceID, setSelectedProvinceID}) => {

    const handleChange = (event: ChangeEvent<HTMLSelectElement, HTMLSelectElement>) => {
        setSelectedProvinceID(event.target.value)
    }

    return (
        <Select onChange={handleChange} value={selectedProvinceID} className={classnames} defaultValue="">
            <option value="" disabled>
                انتخاب استان
            </option>

            {
                provinces.map(p => (
                    <option key={p.id} value={p.id}>
                        {p.name}
                    </option>
                ))
            }
        </Select>
    );
};

export default ProvinceSelect;

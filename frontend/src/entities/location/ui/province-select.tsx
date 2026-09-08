import type { SelectHTMLAttributes } from "react";
import { Select } from "@/shared/ui";
import type { Province } from "../model/types";

interface ProvinceSelectProps extends Omit<SelectHTMLAttributes<HTMLSelectElement>, "children"> {
    provinces: Province[];
}

export function ProvinceSelect({ provinces, ...props }: ProvinceSelectProps) {
    return <Select {...props}>
        <option value="">همه استان‌ها</option>
        {provinces.map((province) => <option key={province.id} value={province.id}>{province.name}</option>)}
    </Select>;
}

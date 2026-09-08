import type { SelectHTMLAttributes } from "react";
import { Select } from "@/shared/ui";
import type { JobCategory } from "../model/types";

interface JobCategorySelectProps extends Omit<SelectHTMLAttributes<HTMLSelectElement>, "children"> {
    categories: JobCategory[];
}

export function JobCategorySelect({ categories, ...props }: JobCategorySelectProps) {
    return <Select {...props}>
        <option value="">همه دسته‌بندی‌ها</option>
        {categories.map((category) => <option key={category.id} value={category.id}>{category.title}</option>)}
    </Select>;
}

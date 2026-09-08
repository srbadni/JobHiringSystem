"use client";

import { Select, type SelectProps } from "@/shared/ui/select";
import type { JobCategory } from "../model/types";

export type JobCategorySelectProps = Omit<SelectProps, "children" | "defaultValue" | "value" | "onChange" | "multiple"> & {
  jobCategories: readonly JobCategory[];
  value: string;
  onValueChange: (value: string) => void;
  placeholder?: string;
};

export function JobCategorySelect({
  jobCategories, value, onValueChange, placeholder = "همهٔ دسته‌بندی‌ها", ...props
}: JobCategorySelectProps) {
  return (
    <Select {...props} value={value} onChange={(event) => onValueChange(event.target.value)}>
      <option value="">{placeholder}</option>
      {value && !jobCategories.some((category) => category.id === value) && (
        <option value={value}>دسته‌بندی انتخاب‌شده</option>
      )}
      {jobCategories.map((category) => (
        <option key={category.id} value={category.id}>{category.title}</option>
      ))}
    </Select>
  );
}

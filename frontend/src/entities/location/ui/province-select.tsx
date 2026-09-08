"use client";

import { Select, type SelectProps } from "@/shared/ui/select";
import type { Province } from "../model/types";

export type ProvinceSelectProps = Omit<SelectProps, "children" | "defaultValue" | "value" | "onChange" | "multiple"> & {
  provinces: readonly Province[];
  value: string;
  onValueChange: (value: string) => void;
  placeholder?: string;
};

export function ProvinceSelect({
  provinces, value, onValueChange, placeholder = "همهٔ استان‌ها", ...props
}: ProvinceSelectProps) {
  return (
    <Select {...props} value={value} onChange={(event) => onValueChange(event.target.value)}>
      <option value="">{placeholder}</option>
      {value && !provinces.some((province) => province.id === value) && (
        <option value={value}>استان انتخاب‌شده</option>
      )}
      {provinces.map((province) => (
        <option key={province.id} value={province.id}>{province.name}</option>
      ))}
    </Select>
  );
}

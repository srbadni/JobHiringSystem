"use client";

import { useEffect, useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { getJobCategories, JobCategorySelect, type JobCategory } from "@/entities/job-category";
import { getProvinces, ProvinceSelect, type Province } from "@/entities/location";
import { routes } from "@/shared/config";
import { PrimaryButton } from "@/shared/ui";
import { CategoryIcon, LocationIcon, SearchIcon } from "@/shared/ui/icons";

interface JobSearchFormProps {
    className?: string;
}

export function JobSearchForm({ className = "" }: JobSearchFormProps) {
    const router = useRouter();
    const [categoryId, setCategoryId] = useState("");
    const [provinceId, setProvinceId] = useState("");
    const [keywords, setKeywords] = useState("");
    const [provinces, setProvinces] = useState<Province[]>([]);
    const [categories, setCategories] = useState<JobCategory[]>([]);
    const [hasLoadError, setHasLoadError] = useState(false);

    useEffect(() => {
        const controller = new AbortController();
        Promise.all([getProvinces(controller.signal), getJobCategories(controller.signal)])
            .then(([nextProvinces, nextCategories]) => {
                setProvinces(nextProvinces);
                setCategories(nextCategories);
            })
            .catch((error: unknown) => {
                if (!(error instanceof DOMException && error.name === "AbortError")) setHasLoadError(true);
            });
        return () => controller.abort();
    }, []);

    function submit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const params = new URLSearchParams();
        if (keywords.trim()) params.set("keywords", keywords.trim());
        if (provinceId) params.append("province_ids", provinceId);
        if (categoryId) params.append("job_category_ids", categoryId);
        router.push(`${routes.jobSearch}?${params.toString()}`);
    }

    return <form onSubmit={submit} className={`flex flex-col rounded-md border border-gray-300 bg-white p-2 ${className}`}>
        <label className="flex h-10 items-center gap-2 py-1">
            <SearchIcon width={18} height={18} color="#667085" />
            <span className="sr-only">عبارت جستجو</span>
            <input value={keywords} onChange={(event) => setKeywords(event.target.value)} placeholder="عنوان شغل، مهارت یا شرکت" className="flex-1 outline-0" />
        </label>
        <label className="flex items-center gap-2 py-1">
            <LocationIcon width={18} height={18} color="#667085" />
            <span className="sr-only">استان</span>
            <ProvinceSelect value={provinceId} onChange={(event) => setProvinceId(event.target.value)} className="border-0" provinces={provinces} />
        </label>
        <label className="flex items-center gap-2 py-1">
            <CategoryIcon width={18} height={18} color="#667085" />
            <span className="sr-only">دسته‌بندی شغلی</span>
            <JobCategorySelect value={categoryId} onChange={(event) => setCategoryId(event.target.value)} className="border-0" categories={categories} />
        </label>
        {hasLoadError && <p role="alert" className="px-2 text-sm text-red-700">بارگذاری فیلترها ناموفق بود؛ همچنان می‌توانید با عبارت دلخواه جستجو کنید.</p>}
        <PrimaryButton type="submit">جستجو</PrimaryButton>
    </form>;
}

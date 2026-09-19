"use client";

import { useId, useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import classNames from "classnames";

import { ProvinceSelect, provinceQueries } from "@/entities/location";
import { JobCategorySelect, jobCategoryQueries } from "@/entities/job-category";

import { PrimaryButton } from "@/shared/ui/button";
import { SearchIcon, LocationIcon, CategoryIcon } from "@/shared/ui/icons";

import {
    buildJobSearchHref,
    emptyJobSearch,
    type JobSearchValues,
} from "../model/search-params";

import { ReferenceStatus } from "./reference-status";
import {useGlobalStatesContext} from "@/_app/providers/global-states-provider";


export interface JobSearchFormProps {
    className?: string;
    initialValues?: JobSearchValues;
}


export function JobSearchForm({
                                  className,
                                  initialValues = emptyJobSearch,
                              }: JobSearchFormProps) {
    const router = useRouter();
    const id = useId();

    const [values, setValues] = useState(initialValues);

    const provinces = useQuery(provinceQueries.all());
    const {jobCategories: categories} = useGlobalStatesContext();


    function submit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        router.push(buildJobSearchHref(values));
    }


    return (
        <form
            role="search"
            aria-label="جستجوی فرصت‌های شغلی"
            onSubmit={submit}
            className={classNames(
                "flex flex-col rounded-md border border-gray-300 bg-surface p-2",
                className
            )}
        >
            <div className="flex h-10 items-center gap-2 py-1">
                <SearchIcon
                    width={18}
                    height={18}
                    className="shrink-0 text-muted"
                    aria-hidden="true"
                />

                <label
                    className="sr-only"
                    htmlFor={`${id}-keywords`}
                >
                    عنوان شغل، مهارت یا شرکت
                </label>

                <input
                    id={`${id}-keywords`}
                    name="keywords"
                    value={values.keywords}
                    onChange={(event) =>
                        setValues({
                            ...values,
                            keywords: event.target.value,
                        })
                    }
                    placeholder="عنوان شغل، مهارت یا شرکت"
                    type="search"
                    className="min-w-0 flex-1 rounded px-1 outline-none focus-visible:ring-2 focus-visible:ring-primary/20"
                />
            </div>


            <div className="flex items-center gap-2 py-1">
                <LocationIcon
                    width={18}
                    height={18}
                    className="shrink-0 text-muted"
                    aria-hidden="true"
                />

                <label
                    className="sr-only"
                    htmlFor={`${id}-province`}
                >
                    استان
                </label>

                <ProvinceSelect
                    id={`${id}-province`}
                    name="province_id"
                    variant="plain"
                    provinces={provinces.data ?? []}
                    value={values.provinceId}
                    onValueChange={(provinceId) =>
                        setValues({
                            ...values,
                            provinceId,
                        })
                    }
                    disabled={
                        provinces.isPending ||
                        (provinces.isError && !provinces.data)
                    }
                    aria-busy={provinces.isFetching}
                    aria-describedby={`${id}-province-status`}
                />
            </div>


            <div className="flex items-center gap-2 py-1">
                <CategoryIcon
                    width={18}
                    height={18}
                    className="shrink-0 text-muted"
                    aria-hidden="true"
                />

                <label
                    className="sr-only"
                    htmlFor={`${id}-category`}
                >
                    دسته‌بندی شغلی
                </label>

                <JobCategorySelect
                    id={`${id}-category`}
                    name="job_category_id"
                    variant="plain"
                    jobCategories={categories}
                    value={values.jobCategoryId}
                    onValueChange={(jobCategoryId) =>
                        setValues({
                            ...values,
                            jobCategoryId,
                        })
                    }
                    disabled={!categories.length}
                    aria-describedby={`${id}-category-status`}
                />
            </div>


            <PrimaryButton type="submit">
                جستجو
            </PrimaryButton>
        </form>
    );
}

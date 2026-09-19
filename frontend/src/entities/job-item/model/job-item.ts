import {SortType} from "@/features/job-search-result/model/type";

export interface JobItem {
    id: string;
    company_id: string;
    company_title: string;
    company_english_title: string;
    company_logo: string | undefined;
    job_category_title: string;
    province_title: string;
    city_title: string;
    salary_title: string;
    job_title: string;
    employment_type: EmploymentType;
    work_mode: WorkModeType;
    created_at: string;
}

export type WorkModeType =
    | "onsite"
    | "remote"
    | "hybrid";

export type EmploymentType =
    | "full_time"
    | "part_time"
    | "internship";

export const employmentTypeLabels: Record<EmploymentType, string> = {
    full_time: "تمام وقت",
    part_time: "پاره وقت",
    internship: "کارآموزی",
};

export const workModeLabels: Record<WorkModeType, string> = {
    onsite: "حضوری",
    remote: "دورکاری",
    hybrid: "ترکیبی",
};

export type JobQueries = {
    keywords: string | null
    province_ids: string[] | null
    job_category_ids: string[] | null
    sort_type: SortType | undefined
}

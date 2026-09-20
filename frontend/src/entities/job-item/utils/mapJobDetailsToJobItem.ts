import {JobDetails} from "@/entities/job-details/model/job-details";
import {JobItem} from "@/entities/job-item/model/job-item";

export function mapJobDetailsToJobItem(job: JobDetails): JobItem {
    return {
        id: job.id,
        company_id: job.id,
        company_title: job.company_title,
        company_english_title: job.company_en_title,
        company_logo: undefined,
        job_category_title: job.job_category,
        province_title: job.province,
        city_title: job.city,
        salary_title: job.salary_range,
        job_title: job.job_title,
        employment_type: job.employment_type,
        work_mode: job.work_mode,
        created_at: job.created_at,
    };
}

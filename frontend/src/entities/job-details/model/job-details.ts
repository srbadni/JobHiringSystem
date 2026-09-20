export interface JobDetails {
    id: string;
    company_title: string;
    company_en_title: string;
    company_activity: string;
    company_employee_count: EmployeeCount;
    city: string;
    province: string;
    job_category: string;
    job_title: string;
    job_description: string;
    company_overview: string;
    employment_type: EmploymentType;
    work_mode: WorkMode;
    salary_range: string;
    work_experience: WorkExperience;
    minimum_education: EducationLevel;
    gender: Gender;
    military_status: MilitaryStatus;
    post_notifications: boolean;
    status: JobStatus;
    created_at: string;
}

export type EmployeeCount =
    | "1_10"
    | "2_10"
    | "11_50"
    | "51_200"
    | "201_500"
    | "500_plus";

export type EmploymentType =
    | "full_time"
    | "part_time"
    | "internship";

export type WorkMode =
    | "onsite"
    | "remote"
    | "hybrid";

export type WorkExperience =
    | "not_important"
    | "less_than_1"
    | "1_3"
    | "3_5"
    | "5_plus";

export type EducationLevel =
    | "not_important"
    | "diploma"
    | "associate"
    | "bachelor"
    | "master"
    | "phd";

export type Gender =
    | "not_important"
    | "male"
    | "female";

export type MilitaryStatus =
    | "not_important"
    | "completed"
    | "exempt";

export type JobStatus =
    | "active"
    | "inactive"
    | "draft";

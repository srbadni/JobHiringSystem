import {httpClient} from "@/shared/api";
import {JobDetails} from "@/entities/job-details/model/job-details";

interface Queries {
    companyName: string,
    jobId: string
}

export const getJobDetailsQuery = async (queries: Queries): Promise<JobDetails> => {
    const result = await httpClient.get(`/applicant/companies/${queries.companyName}/jobs/${queries.jobId}`)
    return result.data;
}

import {AxiosInstance} from "axios";
import {api} from "@/features/shared/http/api";
import JobCategories from "@/entities/job-categories/model/type";

export class JobCategoriesServices {
    api

    constructor(api: AxiosInstance) {
        this.api = api
    }

    get_all = async (): Promise<JobCategories> => {
        const result = await this.api.get("/job-categories")
        return result.data
    }
}

const jobCategoriesServices = new JobCategoriesServices(api)
export default jobCategoriesServices

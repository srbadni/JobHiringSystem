import {api} from "@/features/shared/http/api";
import {AxiosInstance} from "axios";
import {Provinces} from "@/entities/location/model/provinecs";

export class ProvinceServices {
    private api: AxiosInstance;

    constructor(api: AxiosInstance) {
        this.api = api;
    }

    get_all = async (): Promise<Provinces> => {
        const {data} = await this.api.get<Provinces>("/provinces");

        return data;
    };
}

const provinceServices = new ProvinceServices(api);

export default provinceServices;

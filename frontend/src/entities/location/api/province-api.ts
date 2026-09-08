import type { AxiosInstance } from "axios";
import { httpClient } from "@/shared/api";
import type { Province } from "../model/types";

export function createProvinceApi(client: AxiosInstance) {
  return {
    async getAll(signal?: AbortSignal): Promise<Province[]> {
      const { data } = await client.get<Province[]>("/provinces", { signal });
      return data;
    },
  };
}

export const provinceApi = createProvinceApi(httpClient);

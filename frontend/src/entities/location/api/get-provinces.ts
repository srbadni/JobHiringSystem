import { get } from "@/shared/api";
import type { Province } from "../model/types";

export async function getProvinces(signal?: AbortSignal): Promise<Province[]> {
    return get<Province[]>("/provinces", { signal });
}

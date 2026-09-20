"use server";

import { httpClient } from "@/shared/api";

export async function createJobApplication(formData: FormData) {
    const jobId = formData.get("jobId") as string;
    const applicantId = formData.get("applicant_id") as string;

    try {
        await httpClient.post(`/applicant/jobs/${jobId}/applications`, {}, {
            params: {
                job_id: jobId,
            },
            headers: {
                "X-Applicant-Id": applicantId,
            }
        });

        return {
            success: true,
        };

    } catch (error: any) {

        return {
            success: false,
            message:
                error.response?.data?.message ??
                "ثبت درخواست انجام نشد",
            code:
                error.response?.data?.code ?? "UNKNOWN_ERROR"
        };
    }
}

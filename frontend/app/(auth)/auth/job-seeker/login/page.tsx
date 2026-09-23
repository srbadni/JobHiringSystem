import type { Metadata } from "next";
import { AuthPage } from "@/_pages/auth";

export const metadata: Metadata = { title: "ورود کارجو | کارراه" };

export default function Page() {
    return <AuthPage role="job-seeker" mode="login" />;
}

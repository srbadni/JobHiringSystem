import type { Metadata } from "next";
import { AuthPage } from "@/_pages/auth";

export const metadata: Metadata = { title: "ثبت‌نام کارفرما | کارراه" };

export default function Page() {
    return <AuthPage role="employer" mode="register" />;
}

import type { Metadata } from "next";
import { AuthPage } from "@/_pages/auth";

export const metadata: Metadata = { title: "ورود کارفرما | کارراه" };

export default function Page() {
    return <AuthPage role="employer" mode="login" />;
}

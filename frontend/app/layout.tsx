import type {Metadata} from "next";
import type {ReactNode} from "react";
import {Vazirmatn} from "next/font/google";
import {QueryProvider} from "@/_app/providers";
import "@/_app/styles/globals.css";
import {AuthProviderWrapper} from "@/entities/auth/model/auth-provider-wrapper";

const vazirmatn = Vazirmatn({variable: "--font-vazirmatn", subsets: ["arabic"]});
export const metadata: Metadata = {title: "سامانه استخدام", description: "سامانه کاریابی و استخدام"};

export default function RootLayout({children}: { children: ReactNode }) {
    return (
        <html id="top" lang="fa" dir="rtl" className={`${vazirmatn.variable} h-full scroll-smooth antialiased`}>
        <body className="flex min-h-full flex-col">
        <QueryProvider>
            <AuthProviderWrapper>
                {children}
            </AuthProviderWrapper>
        </QueryProvider>
        </body>
        </html>
    );
}

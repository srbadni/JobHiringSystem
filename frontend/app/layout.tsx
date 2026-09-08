import type {Metadata} from "next";
import type {ReactNode} from "react";
import {Vazirmatn} from "next/font/google";
import {QueryProvider} from "@/_app/providers";
import {SiteHeader} from "@/widgets/site-header";
import {SiteFooter} from "@/widgets/site-footer";
import "@/_app/styles/globals.css";
import GlobalStatesProviderWrapper from "@/_app/providers/global-states-provider-wrapper";

const vazirmatn = Vazirmatn({variable: "--font-vazirmatn", subsets: ["arabic"]});
export const metadata: Metadata = {title: "سامانه استخدام", description: "سامانه کاریابی و استخدام"};

export default function RootLayout({children}: { children: ReactNode }) {
    return (
        <html id="top" lang="fa" dir="rtl" className={`${vazirmatn.variable} h-full scroll-smooth antialiased`}>
        <body className="flex min-h-full flex-col">
        <QueryProvider>
            <GlobalStatesProviderWrapper>
                <SiteHeader/>
                {children}
                <SiteFooter/>
            </GlobalStatesProviderWrapper>
        </QueryProvider>
        </body>
        </html>
    );
}

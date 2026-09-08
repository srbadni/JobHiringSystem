import type {Metadata} from "next";
import {Vazirmatn} from "next/font/google";
import "./globals.css";
import Header from "@/features/shared/components/main-header";
import Providers from "@/app/providers";

const vazirmatn = Vazirmatn({
    variable: "--font-vazirmatn",
    subsets: ["arabic"],
});

export const metadata: Metadata = {
    title: "سامانه استخدام",
    description: "سامانه کاریابی و استخدام",
};

export default function RootLayout({children}: LayoutProps<"/">) {
    return (
        <Providers>
            <html
                lang="fa"
                dir="rtl"
                className={`${vazirmatn.variable} h-full antialiased`}
            >
            <body className="min-h-full flex flex-col">
            <Header/>
            {children}
            </body>
            </html>
        </Providers>
    );
}

import type {Metadata} from "next";
import "./globals.css";
import { AppHeader } from "@/widgets/app-header";

export const metadata: Metadata = {
    title: "سامانه استخدام",
    description: "سامانه کاریابی و استخدام",
};

export default function RootLayout({children}: LayoutProps<"/">) {
    return (
        <html
            lang="fa"
            dir="rtl"
            className="h-full antialiased"
        >
            <body className="min-h-full flex flex-col">
                <AppHeader />
                {children}
            </body>
        </html>
    );
}

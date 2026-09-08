import type { Metadata } from "next";
import type { ReactNode } from "react";
import { Vazirmatn } from "next/font/google";
import { QueryProvider } from "@/_app/providers";
import { SiteHeader } from "@/widgets/site-header";
import "@/_app/styles/globals.css";

const vazirmatn = Vazirmatn({ variable: "--font-vazirmatn", subsets: ["arabic"] });
export const metadata: Metadata = { title: "سامانه استخدام", description: "سامانه کاریابی و استخدام" };

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fa" dir="rtl" className={`${vazirmatn.variable} h-full antialiased`}>
      <body className="flex min-h-full flex-col">
        <QueryProvider>
          <SiteHeader />
          {children}
        </QueryProvider>
      </body>
    </html>
  );
}

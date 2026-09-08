import Link from "next/link";
import { routes } from "@/shared/config";
import { Typography } from "@/shared/ui";

export function JobSearchPage() {
    return <main className="px-3 py-8">
        <Typography as="h1" variant="h2">نتایج جستجوی فرصت‌های شغلی</Typography>
        <Typography tone="muted" className="mt-3">فیلترهای انتخاب‌شده در نشانی صفحه نگه‌داری شده‌اند. نمایش فهرست نتایج در برش «جستجوی مشاغل» تکمیل می‌شود.</Typography>
        <Link href={routes.home} className="mt-6 inline-block font-medium text-primary">بازگشت و تغییر جستجو</Link>
    </main>;
}

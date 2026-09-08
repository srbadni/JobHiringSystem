import Link from "next/link";
import { routes } from "@/shared/config";
import { Typography } from "@/shared/ui";
import { MenuIcon } from "@/shared/ui/icons";

export function AppHeader() {
    return <header className="flex items-center bg-white p-2">
        <Link href={routes.home} aria-label="صفحه اصلی" className="font-bold text-primary">کاریاب</Link>
        <Typography className="ms-auto me-4">ورود / ثبت نام</Typography>
        <button type="button" aria-label="باز کردن منو"><MenuIcon /></button>
    </header>;
}

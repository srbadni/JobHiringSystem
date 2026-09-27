import { MenuIcon } from "@/shared/ui/icons";
import { Typography } from "@/shared/ui/typography";

export function SiteHeader() {
  return (
    <header className="flex items-center bg-surface p-2">
      <span>logo</span>
      <Link href="/auth/job-seeker/login" className="ms-auto me-4">
        <Typography>ورود / ثبت نام</Typography>
      </Link>
      <MenuIcon />
    </header>
  );
}
import Link from "next/link";

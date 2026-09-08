import { MenuIcon } from "@/shared/ui/icons";
import { Typography } from "@/shared/ui/typography";

export function SiteHeader() {
  return (
    <header className="flex items-center bg-surface p-2">
      <span>logo</span>
      <Typography className="ms-auto me-4">ورود / ثبت نام</Typography>
      <MenuIcon />
    </header>
  );
}

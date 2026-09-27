import Link from "next/link";
import { BuildingIcon, UserIcon } from "@/shared/ui/icons";
import { getAuthHref, type AuthPageProps } from "../model/auth-page";
import styles from "./auth-form.module.css";

export function AuthRoleSwitch({ role, mode }: AuthPageProps) {
    return (
        <nav className={styles.roles} aria-label="نوع حساب">
            <Link href={getAuthHref("job-seeker", mode)} aria-current={role === "job-seeker" ? "page" : undefined}>
                <UserIcon width={24} height={24} aria-hidden="true" />کارجو هستم
            </Link>
            <Link href={getAuthHref("employer", mode)} aria-current={role === "employer" ? "page" : undefined}>
                <BuildingIcon width={24} height={24} aria-hidden="true" />کارفرما هستم
            </Link>
        </nav>
    );
}

import { CheckIcon } from "@/shared/ui/icons";
import { AuthPreviewCard } from "./auth-preview-card";
import styles from "./auth-showcase.module.css";

const benefits = {
    employer: ["صفحه اختصاصی برای معرفی شرکت", "انتشار و مدیریت فرصت‌های شغلی", "بررسی و پیگیری درخواست‌ها در یک‌جا"],
    "job-seeker": ["یک رزومه برای معرفی مهارت‌هایت", "فرصت‌های شغلی متناسب با مسیر تو", "پیگیری وضعیت درخواست‌های همکاری"],
};

export function AuthShowcase({ role }: { role: "job-seeker" | "employer" }) {
    const employer = role === "employer";

    return (
        <aside className={`${styles.showcase} ${employer ? styles.employer : ""}`} aria-label={employer ? "کارراه برای کارفرماها" : "کارراه برای کارجوها"}>
            <div className={styles.content}>
                <div className={styles.kicker}>
                    <span>{employer ? "برای ساختن تیم بعدی" : "برای قدم بعدی مسیرت"}</span>
                    <span lang="en" dir="ltr">KARRAH / {employer ? "TEAMS" : "CAREERS"}</span>
                </div>
                <h2>{employer ? "آدم‌های مناسب،" : "قدم بعدی تو،"}<br /><span>{employer ? "تیم‌های بهتر می‌سازند." : "یک فرصت تازه است."}</span></h2>
                <p className={styles.description}>
                    {employer ? "شرکتت را معرفی کن و مسیر رسیدن به هم‌تیمی بعدی را ساده‌تر کن." : "توانایی‌هایت را معرفی کن و جایی را پیدا کن که برای رشد تو جا دارد."}
                </p>
                <AuthPreviewCard employer={employer} />
                <ul className={styles.benefits}>
                    {benefits[role].map((benefit) => <li key={benefit}><CheckIcon width={22} height={22} aria-hidden="true" />{benefit}</li>)}
                </ul>
            </div>
        </aside>
    );
}

import Link from "next/link";
import { AuthForm, AuthRoleSwitch, getAuthContent, type AuthPageProps } from "@/features/authentication";
import { AuthShowcase } from "@/widgets/auth-showcase";
import { Brand } from "@/shared/ui/brand";
import { ArrowLeftIcon } from "@/shared/ui/icons";
import { Typography } from "@/shared/ui/typography";
import styles from "./auth-page.module.css";

export function AuthPage({ role, mode }: AuthPageProps) {
    const content = getAuthContent(role, mode);

    return (
        <div className={`${styles.page} ${role === "employer" ? styles.employer : ""}`}>
            <header className={styles.header}>
                <Brand />
                <Link href="/" className={styles.back}>بازگشت به صفحه اصلی<ArrowLeftIcon width={22} height={22} aria-hidden="true" /></Link>
            </header>
            <main className={styles.main}>
                <div className={styles.card}>
                    <section className={styles.formPanel} aria-labelledby="auth-title">
                        <AuthRoleSwitch role={role} mode={mode} />
                        <div className={styles.intro}>
                            <span className={styles.eyebrow}>{content.eyebrow}</span>
                            <Typography as="h1" variant="h1" id="auth-title" className={styles.title}>{content.title}</Typography>
                            <Typography className={styles.description} tone="muted">{content.description}</Typography>
                        </div>
                        <AuthForm key={`${role}-${mode}`} role={role} mode={mode} />
                    </section>
                    <AuthShowcase role={role} />
                </div>
            </main>
            <footer className={styles.footer}>
                <p>کارراه؛ نقطه تلاقی توانایی‌ها و فرصت‌ها.</p>
                <nav aria-label="پیوندهای پایین صفحه"><Link href="/jobs/search">فرصت‌های شغلی</Link><Link href="/#faq">سؤال‌های متداول</Link></nav>
            </footer>
        </div>
    );
}

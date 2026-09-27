import { Input, PasswordInput } from "@/shared/ui/input";
import { CheckIcon } from "@/shared/ui/icons";
import styles from "./auth-form.module.css";

export function EmployerAccountFields() {
    return (
        <div className={`${styles.fields} ${styles.registration}`}>
            <div className={styles.field}>
                <label htmlFor="full-name">نام و نام خانوادگی</label>
                <Input id="full-name" name="fullName" autoComplete="name" placeholder="نام کامل خودت" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="company-name">نام شرکت</label>
                <Input id="company-name" name="companyName" autoComplete="organization" placeholder="نام مجموعه شما" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="email">ایمیل کاری</label>
                <Input id="email" name="email" type="email" dir="ltr" autoComplete="email" placeholder="you@company.com" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="phone">شماره موبایل</label>
                <Input id="phone" name="phone" type="tel" dir="ltr" autoComplete="tel" placeholder="09123456789" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="password">رمز عبور</label>
                <PasswordInput id="password" name="password" autoComplete="new-password" placeholder="یک رمز عبور انتخاب کن" minLength={8} aria-describedby="password-hint" required />
                <span id="password-hint" className={styles.hint}><CheckIcon width={18} height={18} aria-hidden="true" />حداقل ۸ کاراکتر</span>
            </div>
            <div className={styles.field}>
                <label htmlFor="confirm-password">تکرار رمز عبور</label>
                <PasswordInput id="confirm-password" name="confirmPassword" autoComplete="new-password" placeholder="رمز عبور را دوباره وارد کن" minLength={8} required />
            </div>
        </div>
    );
}

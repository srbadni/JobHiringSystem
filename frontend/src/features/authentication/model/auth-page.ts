export type AuthRole = "job-seeker" | "employer";
export type AuthMode = "login" | "register";

export type AuthPageProps = { role: AuthRole; mode: AuthMode };

export function getAuthHref(role: AuthRole, mode: AuthMode) {
    return `/auth/${role}/${mode}`;
}

export function getAuthContent(role: AuthRole, mode: AuthMode) {
    const employer = role === "employer";
    const register = mode === "register";
    const roleLabel = employer ? "کارفرما" : "کارجو";

    return {
        roleLabel,
        title: `${register ? "ثبت‌نام" : "ورود"} ${roleLabel}`,
        eyebrow: register ? "از اینجا شروع کن" : "خوش برگشتی",
        description: register
            ? employer ? "حساب خودت و شرکتت را در یک مرحله بساز." : "اولین قدم برای پیدا کردن فرصت بعدی را بردار."
            : employer ? "برای مدیریت آگهی‌ها و درخواست‌ها وارد شو." : "وارد شو و مسیر شغلی‌ات را ادامه بده.",
        submitLabel: register
            ? employer ? "ساخت حساب و ثبت شرکت" : "ساخت حساب کارجویی"
            : employer ? "ورود به حساب کارفرمایی" : "ورود به حساب کارجویی",
        emailLabel: employer ? "ایمیل کاری" : "ایمیل",
        emailPlaceholder: employer ? "you@company.com" : "you@example.com",
    };
}

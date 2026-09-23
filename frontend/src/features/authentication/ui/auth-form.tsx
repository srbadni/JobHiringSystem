"use client";

import { useState, type FormEvent } from "react";
import Link from "next/link";
import { Button } from "@/shared/ui/button";
import { Input, PasswordInput } from "@/shared/ui/input";
import { ArrowLeftIcon, CheckIcon, InfoIcon } from "@/shared/ui/icons";
import { Typography } from "@/shared/ui/typography";
import { getAuthContent, getAuthHref, type AuthPageProps } from "../model/auth-page";
import styles from "./auth-form.module.css";

export function AuthForm({ role, mode }: AuthPageProps) {
    const register = mode === "register";
    const employer = role === "employer";
    const content = getAuthContent(role, mode);
    const [previewSubmitted, setPreviewSubmitted] = useState(false);

    function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        // Design preview only: never transmit or persist credentials.
        setPreviewSubmitted(true);
    }

    return (
        <>
            <form className={styles.form} onSubmit={handleSubmit} aria-label={content.title}>
                <div className={`${styles.fields} ${register ? styles.registration : ""}`}>
                    {register && (
                        <>
                            <div className={`${styles.field} ${!employer ? styles.fullWidth : ""}`}>
                                <label htmlFor="full-name">نام و نام خانوادگی</label>
                                <Input id="full-name" name="fullName" autoComplete="name" placeholder="نام کامل خودت" required />
                            </div>
                            {employer && (
                                <div className={styles.field}>
                                    <label htmlFor="company-name">نام شرکت</label>
                                    <Input id="company-name" name="companyName" autoComplete="organization" placeholder="نام مجموعه شما" required />
                                </div>
                            )}
                        </>
                    )}
                    <div className={`${styles.field} ${!employer ? styles.fullWidth : ""}`}>
                        <label htmlFor="email">{content.emailLabel}</label>
                        <Input id="email" name="email" type="email" dir="ltr" autoComplete="email" placeholder={content.emailPlaceholder} required />
                    </div>
                    {register && employer && (
                        <div className={styles.field}>
                            <label htmlFor="phone">شماره موبایل</label>
                            <Input id="phone" name="phone" type="tel" dir="ltr" autoComplete="tel" placeholder="09123456789" required />
                        </div>
                    )}
                    <div className={styles.field}>
                        <label htmlFor="password">رمز عبور</label>
                        <PasswordInput
                            id="password" name="password" required
                            autoComplete={register ? "new-password" : "current-password"}
                            placeholder={register ? "یک رمز عبور انتخاب کن" : "رمز عبورت را وارد کن"}
                            minLength={register ? 8 : undefined}
                            aria-describedby={register ? "password-hint" : undefined}
                        />
                        {register && <span id="password-hint" className={styles.hint}><CheckIcon width={18} height={18} aria-hidden="true" />حداقل ۸ کاراکتر</span>}
                    </div>
                    {register && (
                        <div className={styles.field}>
                            <label htmlFor="confirm-password">تکرار رمز عبور</label>
                            <PasswordInput id="confirm-password" name="confirmPassword" autoComplete="new-password" placeholder="رمز عبور را دوباره وارد کن" minLength={8} required />
                        </div>
                    )}
                </div>
                {!register && (
                    <div className={styles.forgot}>
                        <button type="button" disabled title="بازیابی رمز عبور هنوز فعال نیست" aria-label="رمز عبورت را فراموش کرده‌ای؟ (به‌زودی)">
                            رمز عبورت را فراموش کرده‌ای؟
                        </button>
                    </div>
                )}
                <Button type="submit" className={styles.submit}>
                    {content.submitLabel}<ArrowLeftIcon width={24} height={24} aria-hidden="true" />
                </Button>
                {previewSubmitted && <p role="status" className={styles.feedback}>این فرم فعلاً پیش‌نمایش است؛ اطلاعاتی ارسال یا ذخیره نشد.</p>}
            </form>
            <div className={styles.alternate}>
                <span>{register ? "قبلاً ثبت‌نام کرده‌ای؟" : "هنوز حساب نداری؟"}</span>
                <Link href={getAuthHref(role, register ? "login" : "register")}>
                    {register ? "وارد شو" : `ثبت‌نام ${content.roleLabel}`}<ArrowLeftIcon width={24} height={24} aria-hidden="true" />
                </Link>
            </div>
            <div className={styles.notice}>
                <InfoIcon width={18} height={18} aria-hidden="true" />
                <Typography tone="muted" className={styles.noticeText}>
                    پیش‌نمایش طراحی؛ ورود و ثبت‌نام واقعی انجام نمی‌شود. از اطلاعات آزمایشی استفاده کن.
                </Typography>
            </div>
        </>
    );
}

"use client";

import { type FormEvent } from "react";
import Link from "next/link";
import { Button } from "@/shared/ui/button";
import { Input, PasswordInput } from "@/shared/ui/input";
import { ArrowLeftIcon, CheckIcon, InfoIcon } from "@/shared/ui/icons";
import { Typography } from "@/shared/ui/typography";
import { getAuthContent, getAuthHref, type AuthPageProps } from "../model/auth-page";
import styles from "./auth-form.module.css";
import {useMutation} from "@tanstack/react-query";
import {httpClient} from "@/shared/api";
import {LoginPayload, LoginResponse} from "@/features/authentication/model/type";
import {useAuth} from "@/entities/auth/model";

export function AuthForm({ role, mode }: AuthPageProps) {
    const register = mode === "register";
    const employer = role === "employer";
    const content = getAuthContent(role, mode);
    const {setAccessToken} = useAuth()

    const loginMutation = useMutation<LoginResponse, any, Partial<LoginPayload>>({
        mutationKey: ["login"],
        mutationFn: async (variables): Promise<LoginResponse> => {
            const result = await httpClient.post("/auth/login", variables);
            return result.data;
        },
        onSuccess: (data) => {
            setAccessToken(data.access_token)
        }
    })

    function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);

        const data = {
            fullName: String(formData.get("fullName")) || "",
            companyName: String(formData.get("companyName")) || "",
            email: String(formData.get("email")) || "",
            phone: String(formData.get("phone")) || "",
            password: String(formData.get("password")) || "",
            confirmPassword: String(formData.get("confirmPassword")) || "",
        };

        if (register) return;
        loginMutation.mutate({
            email: data.email,
            password: data.password,
        })

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

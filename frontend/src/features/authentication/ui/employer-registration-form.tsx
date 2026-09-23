"use client";

import { type FormEvent, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { ArrowLeftIcon } from "@/shared/ui/icons";
import type { EmployerAccountData, EmployerRegistrationData } from "../model/employer-registration";
import { EmployerAccountFields } from "./employer-account-fields";
import { EmployerCompanyFields } from "./employer-company-fields";
import styles from "./auth-form.module.css";
import registrationStyles from "./employer-registration.module.css";

const steps = ["اطلاعات حساب", "تأیید شماره همراه", "تکمیل اطلاعات شرکت"];

export function EmployerRegistrationForm() {
    const [step, setStep] = useState(0);
    const [account, setAccount] = useState<EmployerAccountData | null>(null);
    const [nameFa, setNameFa] = useState("");
    const [companyNameEdited, setCompanyNameEdited] = useState(false);
    const [feedback, setFeedback] = useState("");
    const headingRef = useRef<HTMLHeadingElement>(null);

    useEffect(() => {
        if (step > 0) headingRef.current?.focus();
    }, [step]);

    function onSubmit(data: EmployerRegistrationData) {
        // TODO: Send data.account and data.company to your registration API here.
        // data.company.logo is File | null; the verification code is intentionally excluded.
        setFeedback(`اطلاعات شرکت «${data.company.nameFa}» آماده ارسال است؛ هنوز ثبت‌نام نهایی انجام نشده است.`);
    }

    function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const form = event.currentTarget;
        const formData = new FormData(form);
        const value = (name: string) => String(formData.get(name) ?? "");
        setFeedback("");

        if (step === 0) {
            const confirmPassword = form.elements.namedItem("confirmPassword") as HTMLInputElement;
            if (value("password") !== value("confirmPassword")) {
                confirmPassword.setCustomValidity("تکرار رمز عبور با رمز عبور یکسان نیست.");
                confirmPassword.reportValidity();
                return;
            }
            setAccount({
                fullName: value("fullName"), companyName: value("companyName"),
                email: value("email"), phone: value("phone"),
                password: value("password"), confirmPassword: value("confirmPassword"),
            });
            if (!companyNameEdited) setNameFa(value("companyName"));
            // Returning to edit account details requires entering a code again.
            (form.elements.namedItem("verificationCode") as HTMLInputElement).value = "";
            setStep(1);
            return;
        }

        if (step === 1) {
            const code = form.elements.namedItem("verificationCode") as HTMLInputElement;
            if (!value("verificationCode").trim()) {
                code.setCustomValidity("کد تأیید را وارد کن.");
                code.reportValidity();
                return;
            }
            // Prototype only: accept any nonempty code without sending/checking an OTP.
            setStep(2);
            return;
        }

        if (!account) return;
        const logo = formData.get("logo");
        onSubmit({
            account,
            company: {
                nameFa: value("nameFa"), nameEn: value("nameEn"),
                logo: logo instanceof File && logo.size > 0 ? logo : null,
                phone: value("companyPhone"), website: value("website"),
                activityCodes: formData.getAll("activityCodes").map(String),
                employeeCount: value("employeeCount"),
            },
        });
    }

    return (
        <>
            <ol className={registrationStyles.steps} aria-label="مراحل ثبت‌نام کارفرما">
                {steps.map((label, index) => (
                    <li key={label} aria-current={step === index ? "step" : undefined} data-complete={step > index}>
                        <span aria-hidden="true">{["۱", "۲", "۳"][index]}</span>{label}
                    </li>
                ))}
            </ol>
            <form className={styles.form} onSubmit={handleSubmit} aria-label="ثبت‌نام کارفرما" onInput={(event) => {
                const form = event.currentTarget;
                (form.elements.namedItem("confirmPassword") as HTMLInputElement).setCustomValidity("");
                (form.elements.namedItem("verificationCode") as HTMLInputElement).setCustomValidity("");
                setFeedback("");
            }}>
                <h2 ref={headingRef} tabIndex={-1} className={registrationStyles.heading}>{steps[step]}</h2>
                {/* Keep fields mounted to preserve values and the selected file when navigating back. */}
                <fieldset hidden={step !== 0} disabled={step !== 0} className={registrationStyles.fieldset}>
                    <legend className="sr-only">اطلاعات حساب</legend>
                    <EmployerAccountFields />
                </fieldset>
                <fieldset hidden={step !== 1} disabled={step !== 1} className={registrationStyles.fieldset}>
                    <legend className="sr-only">تأیید شماره همراه</legend>
                    <p className={registrationStyles.phoneHint}>شماره همراه: <bdi>{account?.phone}</bdi></p>
                    <div className={styles.field}>
                        <label htmlFor="verification-code">کد تأیید</label>
                        <Input id="verification-code" name="verificationCode" autoComplete="one-time-code" inputMode="numeric" dir="ltr" placeholder="کد تأیید را وارد کن" aria-describedby="verification-hint" className={registrationStyles.code} required />
                        <p id="verification-hint" className={registrationStyles.helper}>فعلاً پیامکی ارسال نمی‌شود؛ برای ادامه هر کدی وارد کن و دکمه تأیید را بزن.</p>
                    </div>
                </fieldset>
                <fieldset hidden={step !== 2} disabled={step !== 2} className={registrationStyles.fieldset}>
                    <legend className="sr-only">اطلاعات شرکت</legend>
                    <EmployerCompanyFields nameFa={nameFa} onNameFaChange={(value) => { setNameFa(value); setCompanyNameEdited(true); }} />
                </fieldset>
                <Button type="submit" className={styles.submit}>
                    {step === 0 ? "ساخت حساب و ثبت شرکت" : step === 1 ? "تأیید و ادامه" : "ذخیره اطلاعات شرکت"}
                    <ArrowLeftIcon width={24} height={24} aria-hidden="true" />
                </Button>
                {step > 0 && <Button className={registrationStyles.back} onClick={() => { setFeedback(""); setStep(step - 1); }}>{step === 1 ? "ویرایش اطلاعات و شماره همراه" : "بازگشت به مرحله قبل"}</Button>}
                <p role="status" className={styles.feedback}>{feedback}</p>
            </form>
            <div className={styles.alternate}>
                <span>قبلاً ثبت‌نام کرده‌ای؟</span>
                <Link href="/auth/employer/login">وارد شو<ArrowLeftIcon width={24} height={24} aria-hidden="true" /></Link>
            </div>
        </>
    );
}

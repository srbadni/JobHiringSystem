import { useState } from "react";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Select } from "@/shared/ui/select";
import { companyActivityOptions, employeeCountOptions } from "../model/employer-registration";
import styles from "./auth-form.module.css";
import registrationStyles from "./employer-registration.module.css";

type EmployerCompanyFieldsProps = {
    nameFa: string;
    onNameFaChange: (value: string) => void;
};

export function EmployerCompanyFields({ nameFa, onNameFaChange }: EmployerCompanyFieldsProps) {
    const [hasLogo, setHasLogo] = useState(false);
    const [activities, setActivities] = useState([""]);

    return (
        <div className={styles.fields}>
            <div className={styles.field}>
                <label htmlFor="company-name-fa">نام شرکت به فارسی *</label>
                <Input id="company-name-fa" name="nameFa" value={nameFa} onChange={(event) => onNameFaChange(event.target.value)} autoComplete="organization" placeholder="مثال: کارراه" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="company-name-en">نام شرکت به انگلیسی *</label>
                <Input id="company-name-en" name="nameEn" dir="ltr" placeholder="مثال: Karrah" required />
            </div>
            <div className={styles.field}>
                <span className={registrationStyles.label}>لوگوی شرکت</span>
                <label className={registrationStyles.logoToggle}>
                    <input type="checkbox" role="switch" checked={hasLogo} onChange={(event) => setHasLogo(event.target.checked)} aria-controls="company-logo-field" />
                    فایل لوگوی شرکت را دارم
                </label>
                <div id="company-logo-field" hidden={!hasLogo}>
                    <label htmlFor="company-logo" className={registrationStyles.fileLabel}>انتخاب فایل لوگو *</label>
                    <Input id="company-logo" name="logo" type="file" accept="image/*" required={hasLogo} disabled={!hasLogo} className={registrationStyles.fileInput} />
                </div>
                <p className={registrationStyles.helper}>نمایش لوگو به شناخت بهتر شرکت کمک می‌کند. اگر فایل آماده نیست، می‌توانی بعداً آن را اضافه کنی.</p>
            </div>
            <div className={styles.field}>
                <label htmlFor="company-phone">شماره تماس (محرمانه) *</label>
                <Input id="company-phone" name="companyPhone" type="tel" dir="ltr" placeholder="02133779725" required />
            </div>
            <div className={styles.field}>
                <label htmlFor="company-website">آدرس وب‌سایت شرکت</label>
                <Input id="company-website" name="website" dir="ltr" inputMode="url" placeholder="example.com" />
            </div>
            <div className={styles.field}>
                <span className={registrationStyles.label}>حوزه‌های فعالیت شرکت *</span>
                {activities.map((activity, index) => (
                    <div className={registrationStyles.activityRow} key={index}>
                        <Select
                            name="activityCodes" aria-label={`حوزه فعالیت ${index + 1}`} value={activity} required
                            className={registrationStyles.select}
                            onChange={(event) => setActivities(activities.map((value, position) => position === index ? event.target.value : value))}
                        >
                            <option value="">انتخاب صنعت / حوزه</option>
                            {companyActivityOptions.map((option) => (
                                <option key={option.value} value={option.value} disabled={activities.includes(option.value) && activity !== option.value}>{option.label}</option>
                            ))}
                        </Select>
                        {activities.length > 1 && (
                            <Button className={registrationStyles.textButton} aria-label={`حذف حوزه فعالیت ${index + 1}`} onClick={() => setActivities(activities.filter((_, position) => position !== index))}>حذف</Button>
                        )}
                    </div>
                ))}
                <Button className={registrationStyles.addActivity} disabled={activities.includes("") || activities.length >= companyActivityOptions.length} onClick={() => setActivities([...activities, ""])}>+ اضافه کردن حوزه‌های بیشتر</Button>
            </div>
            <div className={styles.field}>
                <label htmlFor="employee-count">تعداد پرسنل *</label>
                <Select id="employee-count" name="employeeCount" defaultValue="" required className={registrationStyles.select}>
                    <option value="">انتخاب تعداد پرسنل</option>
                    {employeeCountOptions.map((option) => <option key={option.value} value={option.value}>{option.label}</option>)}
                </Select>
            </div>
        </div>
    );
}

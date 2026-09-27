import { ArrowLeftIcon, BookmarkIcon, DocumentIcon } from "@/shared/ui/icons";
import styles from "./auth-showcase.module.css";

export function AuthPreviewCard({ employer }: { employer: boolean }) {
    return (
        <div className={styles.preview}>
            <div className={styles.previewHeader}>
                <span><DocumentIcon width={20} height={20} aria-hidden="true" />{employer ? "یک نگاه به مسیر استخدام" : "فرصت بعدیِ مسیرت"}</span>
                <small>{employer ? "نمونه" : "آگهی نمونه"}</small>
            </div>
            <div className={styles.job}>
                <span className={styles.companyLogo} aria-hidden="true">نـ</span>
                <div>
                    <h3>طراح محصول</h3>
                    <p>{employer ? "تیم طراحی · استودیو نُوا" : "استودیو نُوا · تهران"}</p>
                </div>
                {!employer && <BookmarkIcon className={styles.bookmark} width={19} height={19} aria-hidden="true" />}
            </div>
            {employer ? (
                <ul className={styles.applicants}>
                    <li>
                        <span className={styles.avatar} aria-hidden="true">س</span>
                        <div><strong>سارا احمدی</strong><p>طراح محصول</p></div>
                        <span className={styles.invited}>دعوت به مصاحبه</span>
                    </li>
                    <li>
                        <span className={`${styles.avatar} ${styles.lilac}`} aria-hidden="true">م</span>
                        <div><strong>محمد رضایی</strong><p>طراح تجربه کاربری</p></div>
                        <span className={styles.reviewing}>در حال بررسی</span>
                    </li>
                </ul>
            ) : (
                <>
                    <div className={styles.tags}><span>دورکاری</span><span>تمام‌وقت</span><span dir="ltr">UI / UX</span><span>Figma</span></div>
                    <div className={styles.cardFooter}><span>جای مهارت تو اینجاست.</span><ArrowLeftIcon width={20} height={20} aria-hidden="true" /></div>
                </>
            )}
        </div>
    );
}

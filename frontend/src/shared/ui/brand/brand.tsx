import Link from "next/link";
import styles from "./brand.module.css";

export function Brand() {
    return (
        <Link href="/" className={styles.brand} aria-label="کارراه، صفحه اصلی">
            <span className={styles.mark} aria-hidden="true"><i /><i /><i /><i /></span>
            <span>کارراه<span className={styles.dot} aria-hidden="true" /></span>
        </Link>
    );
}

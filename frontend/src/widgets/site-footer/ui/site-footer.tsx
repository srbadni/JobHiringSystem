import Link from "next/link";

const jobSeekerLinks = [
    {label: "جست‌وجوی شغل", href: "/jobs/search"},
    {label: "آشنایی با شرکت‌ها", href: "#companies"},
    {label: "فرصت‌های نشان‌شده", href: "#saved-jobs"},
] as const;

const employerLinks = [
    {label: "شروع استخدام", href: "#start-hiring"},
    {label: "ثبت شرکت", href: "#register-company"},
    {label: "انتشار آگهی شغلی", href: "#post-job"},
] as const;

const aboutLinks = [
    {label: "نحوه کار", href: "#how-it-works"},
    {label: "سؤال‌های متداول", href: "#faq"},
    {label: "درباره این طرح", href: "#about"},
] as const;

type FooterLinkGroupProps = {
    title: string;
    links: ReadonlyArray<{label: string; href: string}>;
};

function FooterLinkGroup({title, links}: FooterLinkGroupProps) {
    return (
        <nav aria-label={title}>
            <h2 className="mb-5 text-body-lg font-bold text-foreground">{title}</h2>
            <ul className="space-y-3 text-body-lg text-muted md:text-body">
                {links.map((link) => (
                    <li key={link.label}>
                        <Link className="transition-colors hover:text-primary focus-visible:text-primary" href={link.href}>
                            {link.label}
                        </Link>
                    </li>
                ))}
            </ul>
        </nav>
    );
}

function FooterBrand() {
    return (
        <div>
            <Link className="inline-flex items-end gap-2" href="/" aria-label="کارراه، صفحه اصلی">
                <span className="relative mb-1 grid h-8 w-8 grid-cols-2 gap-1" aria-hidden="true">
                    <span className="rounded-[3px] bg-primary" />
                    <span className="rounded-[3px] bg-secondary" />
                    <span className="rounded-[3px] bg-[#9caaf7]" />
                    <span className="rounded-[3px] bg-primary" />
                    <span className="absolute -right-3 bottom-0 h-2 w-2 bg-primary" />
                </span>
                <span className="text-brand-mobile font-bold leading-none tracking-[-0.04em] text-foreground md:text-brand">
                    کارراه
                </span>
            </Link>
            <p className="mt-6 text-body-lg leading-extra-readable text-muted md:mt-7 md:text-body">
                نقطه تلاقی توانایی‌ها و فرصت‌ها.
                <br />
                برای قدم بعدی مسیر کاری تو.
            </p>
        </div>
    );
}

export function SiteFooter() {
    return (
        <footer className="mt-auto border-t border-border bg-surface px-5 pb-4 pt-16 md:px-8 md:pb-5 md:pt-11">
            <div className="mx-auto max-w-[1240px]">
                <div className="grid grid-cols-2 gap-x-12 gap-y-10 md:grid-cols-4 md:gap-x-20">
                    <div className="col-span-2 md:col-span-1">
                        <FooterBrand />
                    </div>
                    <FooterLinkGroup title="برای کارجوها" links={jobSeekerLinks} />
                    <FooterLinkGroup title="برای کارفرماها" links={employerLinks} />
                    <FooterLinkGroup title="درباره کارراه" links={aboutLinks} />
                </div>

                <div className="mt-11 grid grid-cols-2 gap-y-4 border-t border-border pt-6 text-footer-caption leading-readable text-muted md:mt-8 md:grid-cols-3 md:items-center md:pt-5">
                    <p>کارراه؛ برای قدم بعدی تو.</p>
                    <p className="order-3 col-span-2 md:order-none md:col-span-1 md:text-center">پیش‌نمایش طراحی - شرکت‌ها و آگهی‌ها نمونه هستند</p>
                    <a className="order-2 justify-self-end transition-colors hover:text-primary focus-visible:text-primary md:order-none" href="#top">
                        بازگشت به بالا ↑
                    </a>
                </div>
            </div>
        </footer>
    );
}

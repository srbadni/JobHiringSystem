import type { SVGProps } from "react";

export function EyeIcon({ closed = false, ...props }: SVGProps<SVGSVGElement> & { closed?: boolean }) {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" {...props}>
            <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z" />
            <circle cx="12" cy="12" r="3" />
            {closed && <path d="m3 3 18 18" />}
        </svg>
    );
}

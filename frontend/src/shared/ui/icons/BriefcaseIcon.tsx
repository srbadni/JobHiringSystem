import { SVGProps } from "react";

export function BriefcaseIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <rect
                x="3"
                y="7"
                width="18"
                height="13"
                rx="2"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M9 7V5.5C9 4.67 9.67 4 10.5 4h3c.83 0 1.5.67 1.5 1.5V7"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M3 12h18"
                stroke="currentColor"
                strokeWidth="1.8"
            />
        </svg>
    );
}

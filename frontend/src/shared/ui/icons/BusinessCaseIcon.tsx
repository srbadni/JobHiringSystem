import { SVGProps } from "react";

export function BusinessCaseIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <rect
                x="3"
                y="6"
                width="18"
                height="14"
                rx="2"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M9 6V4.5C9 3.67 9.67 3 10.5 3h3c.83 0 1.5.67 1.5 1.5V6"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M3 11h18M10 14h4"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
            />
        </svg>
    );
}

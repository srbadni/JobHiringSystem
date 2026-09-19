import { SVGProps } from "react";

export function UsersIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <path
                d="M16 20v-1.5c0-2-1.8-3.5-4-3.5s-4 1.5-4 3.5V20"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
            />
            <circle
                cx="12"
                cy="8"
                r="3"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M18 10a2.5 2.5 0 0 0 0-5M20 20v-1c0-1.5-.8-2.6-2-3.2M6 10a2.5 2.5 0 0 1 0-5M4 20v-1c0-1.5.8-2.6 2-3.2"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
            />
        </svg>
    );
}

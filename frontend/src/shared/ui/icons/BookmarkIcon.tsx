import { SVGProps } from "react";

export function BookmarkIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <path
                d="M6 3.5C6 2.67 6.67 2 7.5 2h9c.83 0 1.5.67 1.5 1.5V21l-6-4-6 4V3.5Z"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinejoin="round"
            />
        </svg>
    );
}

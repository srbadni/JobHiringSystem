import { SVGProps } from "react";

export function LaptopIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <rect
                x="5"
                y="3"
                width="14"
                height="12"
                rx="1"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M3 19h18l-2-4H5l-2 4Z"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinejoin="round"
            />
        </svg>
    );
}

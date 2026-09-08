import type { SVGProps } from "react";

export function CategoryIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <rect
                x="4"
                y="4"
                width="6"
                height="6"
                rx="1.2"
                stroke="currentColor"
                strokeWidth="1.8"
            />

            <rect
                x="14"
                y="4"
                width="6"
                height="6"
                rx="1.2"
                stroke="currentColor"
                strokeWidth="1.8"
            />

            <rect
                x="4"
                y="14"
                width="6"
                height="6"
                rx="1.2"
                stroke="currentColor"
                strokeWidth="1.8"
            />

            <rect
                x="14"
                y="14"
                width="6"
                height="6"
                rx="1.2"
                stroke="currentColor"
                strokeWidth="1.8"
            />
        </svg>
    );
}

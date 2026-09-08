// shared/ui/icons/LocationIcon.tsx

import type { SVGProps } from "react";

export function LocationIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M12 21C12 21 19 14.5 19 9.5C19 5.91 15.87 3 12 3C8.13 3 5 5.91 5 9.5C5 14.5 12 21 12 21Z"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
                strokeLinejoin="round"
            />

            <circle
                cx="12"
                cy="9.5"
                r="2.5"
                stroke="currentColor"
                strokeWidth="1.8"
            />
        </svg>
    );
}

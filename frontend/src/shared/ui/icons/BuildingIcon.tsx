import { SVGProps } from "react";

export function BuildingIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <path
                d="M4 21V5.5C4 4.67 4.67 4 5.5 4h9c.83 0 1.5.67 1.5 1.5V21"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M16 9h3c.55 0 1 .45 1 1v11"
                stroke="currentColor"
                strokeWidth="1.8"
            />
            <path
                d="M8 8h2M8 12h2M8 16h2M12 8h2M12 12h2"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
            />
            <path
                d="M3 21h18"
                stroke="currentColor"
                strokeWidth="1.8"
            />
        </svg>
    );
}

import { SVGProps } from "react";

interface FilterIconProps extends SVGProps<SVGSVGElement> {
    width?: number;
    height?: number;
}

export function FilterIcon({
                               width = 24,
                               height = 24,
                               ...props
                           }: FilterIconProps) {
    return (
        <svg
            width={width}
            height={height}
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M4 7H14"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
            />

            <path
                d="M18 7H20"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
            />

            <circle
                cx="16"
                cy="7"
                r="2"
                stroke="currentColor"
                strokeWidth="2"
            />

            <path
                d="M4 17H8"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
            />

            <path
                d="M12 17H20"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
            />

            <circle
                cx="10"
                cy="17"
                r="2"
                stroke="currentColor"
                strokeWidth="2"
            />
        </svg>
    );
}

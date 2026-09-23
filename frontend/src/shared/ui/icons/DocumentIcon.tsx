import type { SVGProps } from "react";

export function DocumentIcon(props: SVGProps<SVGSVGElement>) {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" {...props}>
            <path d="M5 2h9l5 5v15H5V2Zm9 0v6h5M8 12h8m-8 4h6" />
        </svg>
    );
}

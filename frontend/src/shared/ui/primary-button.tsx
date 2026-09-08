import type { ButtonHTMLAttributes } from "react";

export function PrimaryButton({ className = "", ...props }: ButtonHTMLAttributes<HTMLButtonElement>) {
    return <button className={`bg-primary rounded-md py-2 text-white transition-colors hover:bg-primary-hover ${className}`} {...props} />;
}

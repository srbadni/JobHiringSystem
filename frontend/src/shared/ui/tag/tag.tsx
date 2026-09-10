import { ReactNode } from "react";
import classNames from "classnames";

interface TagProps {
    children: ReactNode;
    icon?: ReactNode;
    variant?: "warning" | "success" | "info" | "danger";
    className?: string;
}

const variants = {
    warning: {
        wrapper: "bg-[#FFF8E8] border-[#F4DFA8] text-[#B8862D]",
    },
    success: {
        wrapper: "bg-[#EAFBF0] border-[#B7E8C5] text-[#1E8E4D]",
    },
    info: {
        wrapper: "bg-[#EDF5FF] border-[#C7DDFF] text-[#2563EB]",
    },
    danger: {
        wrapper: "bg-[#FFF0F0] border-[#FFCACA] text-[#DC2626]",
    },
};

export function Tag({
                        children,
                        icon,
                        variant = "warning",
                        className,
                    }: TagProps) {
    return (
        <div
            className={classNames(
                "inline-flex items-center gap-1.5 rounded-md border px-3 py-1 text-xs font-medium",
                variants[variant].wrapper,
                className
            )}
        >
            {icon && (
                <span className="flex items-center justify-center">
                    {icon}
                </span>
            )}

            <span>{children}</span>
        </div>
    );
}

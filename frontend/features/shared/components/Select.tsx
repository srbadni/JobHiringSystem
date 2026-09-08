import { forwardRef, type SelectHTMLAttributes } from "react";

interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement> {
    className?: string;
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
    ({ className = "", children, ...props }, ref) => {
        return (
            <select
                ref={ref}
                {...props}
                className={`
                    h-10
                    w-full
                    rounded-xl
                    border
                    border-gray-200
                    bg-white
                    px-4
                    text-sm
                    text-gray-700
                    outline-none
                    transition-colors

                    focus:border-primary
                    focus:ring-2
                    focus:ring-primary/20

                    disabled:cursor-not-allowed
                    disabled:opacity-50

                    ${className}
                `}
            >
                {children}
            </select>
        );
    }
);

Select.displayName = "Select";

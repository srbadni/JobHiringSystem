import classNames from "classnames";
import type { ComponentPropsWithRef } from "react";

export type ButtonProps = ComponentPropsWithRef<"button">;

export function Button({ type = "button", className, ...props }: ButtonProps) {
    return (
        <button
            {...props}
            type={type}
            className={classNames(
                "inline-flex items-center justify-center rounded-md px-4 py-2 transition-colors focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:cursor-not-allowed disabled:opacity-50",
                className,
            )}
        />
    );
}

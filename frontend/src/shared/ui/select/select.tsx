import classNames from "classnames";
import type { ComponentPropsWithRef } from "react";

export type SelectProps = ComponentPropsWithRef<"select"> & {
  variant?: "outlined" | "plain";
};

export function Select({ variant = "outlined", className, ...props }: SelectProps) {
  return (
    <select
      {...props}
      className={classNames(
        "h-10 w-full min-w-0 rounded-xl bg-surface px-4 text-sm text-foreground outline-none transition-colors focus-visible:ring-2 focus-visible:ring-primary/20 disabled:cursor-not-allowed disabled:opacity-50",
        variant === "outlined" ? "border border-border focus:border-primary" : "border-0",
        className,
      )}
    />
  );
}

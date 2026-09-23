import classNames from "classnames";
import type { ComponentPropsWithRef } from "react";
import styles from "./input.module.css";

export type InputProps = ComponentPropsWithRef<"input">;

export function Input({ className, ...props }: InputProps) {
    return <input {...props} className={classNames(styles.input, className)} />;
}

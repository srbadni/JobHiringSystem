"use client";

import { useState } from "react";
import { Button } from "@/shared/ui/button";
import { EyeIcon } from "@/shared/ui/icons";
import { Input, type InputProps } from "./input";
import styles from "./input.module.css";

export function PasswordInput(props: Omit<InputProps, "type">) {
    const [visible, setVisible] = useState(false);

    return (
        <div className={styles.password}>
            <Input {...props} type={visible ? "text" : "password"} />
            <Button
                className={styles.toggle}
                aria-label={visible ? "پنهان کردن رمز عبور" : "نمایش رمز عبور"}
                aria-pressed={visible}
                aria-controls={props.id}
                onClick={() => setVisible(!visible)}
            >
                <EyeIcon closed={visible} width={22} height={22} aria-hidden="true" />
            </Button>
        </div>
    );
}

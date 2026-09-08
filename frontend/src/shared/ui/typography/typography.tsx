import { createElement, type ComponentPropsWithRef, type ElementType, type JSX } from "react";

const variants = {
    display: "text-display leading-[1.2]",

    h1: "text-[clamp(30px,5vw,52px)] leading-[1.2]",

    h2: "text-section-title-mobile md:text-section-title leading-[1.4]",

    h3: "text-xl leading-[1.5]",

    h4: "text-lg leading-normal",

    h5: "text-base leading-normal",

    h6: "text-sm leading-normal",

    lead: "text-body-lg-mobile md:text-body-lg leading-readable",

    body: "text-body leading-base",

    small: "text-meta leading-readable",

    caption: "text-footer-caption leading-readable",

    code: "font-mono text-meta leading-normal",
} as const;

const tones = {
    inherit: "text-inherit",

    default: "text-foreground",

    muted: "text-muted",

    primary: "text-primary",

    secondary: "text-secondary",

    success: "text-green-700",

    warning: "text-yellow-700",

    danger: "text-red-700",
} as const;

const weights = {
    normal: "font-normal",

    medium: "font-medium",

    semibold: "font-semibold",

    bold: "font-bold",
} as const;

const defaultWeights: Record<
    keyof typeof variants,
    keyof typeof weights
> = {
    display: "bold",

    h1: "bold",

    h2: "bold",

    h3: "semibold",

    h4: "semibold",

    h5: "medium",

    h6: "medium",

    lead: "normal",

    body: "normal",

    small: "normal",

    caption: "normal",

    code: "normal",
};

const alignments = {
    start: "text-start",

    center: "text-center",

    end: "text-end",

    justify: "text-justify",
} as const;

const wraps = {
    normal: "text-wrap",

    balance: "text-balance",

    pretty: "text-pretty",

    nowrap: "text-nowrap",
} as const;

const clamps = {
    1: "line-clamp-1",

    2: "line-clamp-2",

    3: "line-clamp-3",

    4: "line-clamp-4",

    5: "line-clamp-5",

    6: "line-clamp-6",
} as const;

export type TypographyTag = keyof JSX.IntrinsicElements;

export type TypographyVariant = keyof typeof variants;

type TypographyOwnProps = {
    variant?: TypographyVariant;

    tone?: keyof typeof tones;

    weight?: keyof typeof weights;

    align?: keyof typeof alignments;

    wrap?: keyof typeof wraps;

    italic?: boolean;

    underline?: boolean;

    className?: string;
};

type OverflowProps =
    | {
    truncate?: false;

    clamp?: keyof typeof clamps;
}
    | {
    truncate: true;

    clamp?: never;
};

export type TypographyProps<
    T extends ElementType = "p"
> =
    TypographyOwnProps &
    OverflowProps &
    {
        as?: T;
    } &
    Omit<
        ComponentPropsWithRef<T>,
        keyof TypographyOwnProps |
        keyof OverflowProps |
        "as"
    >;

export function Typography<
    T extends ElementType = "p"
>({
      as,

      variant = "body",

      tone = "default",

      weight,

      align = "start",

      wrap,

      italic,

      underline,

      truncate,

      clamp,

      className,

      ...props

  }: TypographyProps<T>) {

    const Component = as ?? "p";

    return createElement(Component, {

        ...props,

        className: [

            "m-0 min-w-0",

            variants[variant],

            tones[tone],

            alignments[align],

            weights[
            weight ?? defaultWeights[variant]
                ],

            !truncate && wrap && wraps[wrap],

            italic && "italic",

            underline && "underline underline-offset-4",

            truncate && "block truncate",

            clamp && clamps[clamp],

            className,

        ]
            .filter(Boolean)
            .join(" "),
    });
}

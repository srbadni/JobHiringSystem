"use client"
import React from 'react';
import {Typography} from "@/shared/ui/typography";
import {useRouter} from "next/navigation";

const BackButton = ({title}: {title: string}) => {
    const router = useRouter()
    return (
        <Typography onClick={router.back} tone="muted" variant="small" as="span">
            {title}
        </Typography>
    );
};

export default BackButton;

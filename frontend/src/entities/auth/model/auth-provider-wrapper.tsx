"use client"

import {AuthProvider} from "@/entities/auth/model/auth-provider";
import {FC, PropsWithChildren} from "react";

export const AuthProviderWrapper: FC<PropsWithChildren> = ({children}) => {
    return (
        <AuthProvider>
            {children}
        </AuthProvider>
    )
}

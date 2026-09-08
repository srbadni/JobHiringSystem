"use client"

import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {PropsWithChildren, useState} from "react";

interface ProvidersProps {

}

export default function Providers(props: PropsWithChildren<ProvidersProps>) {

    const [queryClient] = useState(
        () => new QueryClient()
    );

    return <QueryClientProvider client={queryClient}>
        {props.children}
    </QueryClientProvider>
}

import type { ReactNode } from "react";
import GlobalStatesProviderWrapper from "@/_app/providers/global-states-provider-wrapper";
import { SiteHeader } from "@/widgets/site-header";
import { SiteFooter } from "@/widgets/site-footer";

export default function SiteLayout({ children }: { children: ReactNode }) {
    return (
        <GlobalStatesProviderWrapper>
            <SiteHeader />
            {children}
            <SiteFooter />
        </GlobalStatesProviderWrapper>
    );
}

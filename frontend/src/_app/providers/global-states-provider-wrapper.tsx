import {FC, PropsWithChildren} from "react";
import GlobalStatesProvider from "@/_app/providers/global-states-provider";
import {jobCategoryApi} from "@/entities/job-category";

interface GlobalStatesProviderWrapperProps {

}

async function GlobalStatesProviderWrapper(props: PropsWithChildren<GlobalStatesProviderWrapperProps>){
    const {children} = props;
    const jobCategories = await jobCategoryApi.getAll()

    return (
        <GlobalStatesProvider jobCategories={jobCategories}>
            {children}
        </GlobalStatesProvider>
    );
};

export default GlobalStatesProviderWrapper;

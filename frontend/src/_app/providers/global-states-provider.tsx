"use client"
import {createContext, FC, PropsWithChildren, useContext} from 'react';
import {JobCategory} from "@/entities/job-category";

interface GlobalStatesContextType {
    jobCategories: JobCategory[]
}

interface GlobalStatesProviderProps {
    jobCategories: JobCategory[]
}

const GlobalStatesContext = createContext<GlobalStatesContextType | null>(null);

const GlobalStatesProvider:FC<PropsWithChildren<GlobalStatesProviderProps>> = ({children, jobCategories}) => {
    return <GlobalStatesContext.Provider value={{
        jobCategories,
    }}>
        {children}
    </GlobalStatesContext.Provider>
}

const useGlobalStatesContext = () => {
    const context = useContext(GlobalStatesContext)
    if (!context) {
        throw Error("")
    }
    return context
}

export {useGlobalStatesContext}

export default GlobalStatesProvider;

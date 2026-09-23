import {
    type FC,
    type PropsWithChildren,
    useCallback, useEffect,
    useMemo,
    useState,
} from "react";

import { localStorageService } from "@/shared/lib/storage/local-storage.service";
import { AuthContext } from "./auth-context";
import type { User } from "./auth.types";
import {useQuery} from "@tanstack/react-query";
import {httpClient} from "@/shared/api";

const ACCESS_TOKEN_KEY = "access_token";
const USER_KEY = "user";

export const AuthProvider: FC<PropsWithChildren> = ({ children }) => {
    const [accessToken, setAccessTokenState] = useState<string | null>(
        () => localStorageService.get<string>(ACCESS_TOKEN_KEY),
    );

    const [user, setUserState] = useState<User | null>(
        () => localStorageService.get<User>(USER_KEY),
    );

    const setUser = useCallback((user: User) => {
        localStorageService.set(USER_KEY, user);
        setUserState(user);
    }, []);

    const setAccessToken = useCallback((token: string) => {
        localStorageService.set(ACCESS_TOKEN_KEY, token);
        setAccessTokenState(token);
    }, []);

    const logout = useCallback(() => {
        localStorageService.remove(ACCESS_TOKEN_KEY);
        localStorageService.remove(USER_KEY);

        setAccessTokenState(null);
        setUserState(null);
    }, []);

    const value = useMemo(
        () => ({
            user,
            accessToken,
            isAuthenticated: Boolean(accessToken && user),
            setAccessToken,
            setUser,
            logout,
        }),
        [user, accessToken, setAccessToken, setUser, logout],
    );

    const {dataUpdatedAt, errorUpdatedAt, isSuccess, isError, data} = useQuery({
        queryKey: ["users", accessToken],
        queryFn: async () => {
            const result = await httpClient.get("/auth/users/me");
            return result.data;
        },
        enabled: !!accessToken,
    })

    useEffect(() => {
        if (isSuccess) {
            setUser(data)
        }
    }, [dataUpdatedAt]);

    useEffect(() => {
        if (isError) {
            logout()
        }
    }, [errorUpdatedAt]);

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

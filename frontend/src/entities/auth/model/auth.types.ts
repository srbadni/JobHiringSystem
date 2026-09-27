export interface User {
    id: string;
    full_name: string;
    phone_number: string;
    email: string;
    user_type: "applicant" | "employer";
    profile_image_url: string | null;
}

export interface AuthPayload {
    accessToken: string;
    user: User;
}

export interface AuthContextValue {
    user: User | null;
    accessToken: string | null;
    isAuthenticated: boolean;
    setAccessToken: (accessToken: string) => void;
    setUser: (user: User) => void;
    logout: () => void;
}

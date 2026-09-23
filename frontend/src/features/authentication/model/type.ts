export interface LoginPayload {
    fullName: string
    companyName: string
    email: string
    phone: string
    password: string
    confirmPassword: string
}

export interface LoginResponse {
    access_token: string
    token_type: string
}

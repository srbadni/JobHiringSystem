export interface EmployerAccountData {
    fullName: string;
    companyName: string;
    email: string;
    phone: string;
    password: string;
    confirmPassword: string;
}

export interface EmployerRegistrationData {
    account: EmployerAccountData;
    company: {
        nameFa: string;
        nameEn: string;
        logo: File | null;
        phone: string;
        website: string;
        activityCodes: string[];
        employeeCount: string;
    };
}

// UI-only choices. Replace with company-activity options from the API at integration time.
export const companyActivityOptions = [
    { value: "technology", label: "فناوری اطلاعات و نرم‌افزار" },
    { value: "commerce", label: "بازرگانی و تجارت" },
    { value: "industry", label: "صنعت و تولید" },
    { value: "education", label: "آموزش و پژوهش" },
    { value: "healthcare", label: "سلامت و درمان" },
    { value: "tourism", label: "گردشگری و هتلداری" },
    { value: "finance", label: "مالی و حسابداری" },
    { value: "services", label: "خدمات" },
];

// Values match backend/src/domain/company/enums.py.
export const employeeCountOptions = [
    { value: "2_10", label: "۲ تا ۱۰ نفر" },
    { value: "11_50", label: "۱۱ تا ۵۰ نفر" },
    { value: "51_200", label: "۵۱ تا ۲۰۰ نفر" },
    { value: "201_500", label: "۲۰۱ تا ۵۰۰ نفر" },
    { value: "501_1000", label: "۵۰۱ تا ۱۰۰۰ نفر" },
    { value: "1000_PLUS", label: "بیش از ۱۰۰۰ نفر" },
];

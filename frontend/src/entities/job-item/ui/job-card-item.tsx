"use client"

import Image from "next/image";
import {
    createContext,
    FC,
    PropsWithChildren,
    ReactNode,
    useContext,
} from "react";
import {employmentTypeLabels, JobItem, workModeLabels} from "@/entities/job-item/model/job-item";
import {PrimaryButton} from "@/shared/ui/button";
import {BriefcaseIcon} from "@/shared/ui/icons/BriefcaseIcon";
import {BookmarkIcon} from "@/shared/ui/icons/BookmarkIcon";
import {DEFAULT_COMPANY_LOGO, LocationIcon} from "@/shared/ui/icons";
import SearchTag from "@/shared/ui/tag/search-tag";
import {Typography} from "@/shared/ui/typography";
import {timeAgo} from "@/shared/utils/datetime";
import {useRouter} from "next/navigation";
import classNames from "classnames";

interface JobCardContextValue {
    job: JobItem;
    detailUrl: string;
}

const JobCardContext = createContext<JobCardContextValue | null>(null);

const useJobCard = () => {
    const context = useContext(JobCardContext);

    if (!context) {
        throw new Error("JobCardItem compound components must be used inside JobCardItem.Root");
    }

    return context;
};

interface JobCardRootProps extends PropsWithChildren {
    job: JobItem;
    detailUrl: string;
    className?: string
}

const Root: FC<JobCardRootProps> = ({job, children, detailUrl, className}) => (
    <JobCardContext.Provider value={{job, detailUrl}}>
        <div className={classNames("bg-white border border-gray-200 rounded-lg p-3 flex flex-col", className)}>
            {children}
        </div>
    </JobCardContext.Provider>
);

const Header: FC<PropsWithChildren> = ({children}) => (
    <div className="pb-3 border-b border-gray-200">{children}</div>
);

const Overview: FC<PropsWithChildren> = ({children}) => (
    <div className="flex gap-3 pb-1">{children}</div>
);

const CompanyLogo: FC = () => {
    const {job} = useJobCard();

    return (
        <Image
            src={job.company_logo || DEFAULT_COMPANY_LOGO}
            className="h-[45px] w-[45px] rounded-lg"
            alt={job.company_title}
            width={45}
            height={45}
        />
    );
};

const Information: FC<PropsWithChildren> = ({children}) => (
    <div className="flex flex-col">{children}</div>
);

const Title: FC = () => {
    const {job} = useJobCard();

    return <Typography variant="lead" className="!font-bold">{job.job_title}</Typography>;
};

const CompanyName: FC = () => {
    const {job} = useJobCard();

    return (
        <Typography variant="caption" tone="muted">
            {job.company_title} | {job.company_english_title}
        </Typography>
    );
};

const JobDetails: FC = () => {
    const {job} = useJobCard();

    return (
        <div className="inline-flex gap-3">
            <span className="inline-flex items-center gap-1">
                <LocationIcon className="text-muted" width={14} height={14} />
                <Typography variant="caption" tone="muted">
                    {job.province_title}، {job.city_title}
                </Typography>
            </span>
            <span className="inline-flex items-center gap-1">
                <BriefcaseIcon className="text-muted" width={14} height={14} />
                <Typography variant="caption" tone="muted">
                    {employmentTypeLabels[job.employment_type]}
                </Typography>
            </span>
        </div>
    );
};

const Bookmark: FC = () => (
    <div className="ms-auto">
        <BookmarkIcon width={18} height={18} className="text-muted" />
    </div>
);

const Tags: FC<{children?: ReactNode}> = ({children}) => {
    const {job} = useJobCard();

    return (
        <div className="flex gap-2">
            {children ?? <SearchTag bgMode="muted">{workModeLabels[job.work_mode]}</SearchTag>}
        </div>
    );
};

const Footer: FC<PropsWithChildren> = ({children}) => (
    <div className="flex justify-between items-center pt-2">{children}</div>
);

const Salary: FC = () => {
    const {job} = useJobCard();

    return (
        <div className="flex flex-col pt-2">
            <Typography className="!font-bold" variant="small">
                {job.salary_title}
            </Typography>
            <Typography tone="muted" variant="small">
                {timeAgo(job.created_at)}
            </Typography>
        </div>
    );
};

const ApplyButton: FC = () => {
    const {job, detailUrl} = useJobCard();
    const router = useRouter();

    const onApply = (j: JobItem) => {
        router.push(detailUrl)
    }

    return (
        <PrimaryButton onClick={() => onApply(job)}>
            <Typography className="text-white !font-bold" variant="small">
                ارسال رزومه
            </Typography>
        </PrimaryButton>
    );
};

const JobCardItem = {
    Root,
    Header,
    Overview,
    CompanyLogo,
    Information,
    Title,
    CompanyName,
    JobDetails,
    Bookmark,
    Tags,
    Footer,
    Salary,
    ApplyButton,
};

export default JobCardItem;

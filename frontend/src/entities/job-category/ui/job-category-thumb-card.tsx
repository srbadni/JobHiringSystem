import {FC, ReactNode} from "react";
import {Typography} from "@/shared/ui/typography";
import Link from "next/link";

interface JobCategoryThumbCardProps {
    logo: ReactNode,
    title: string
    url: string
}

const JobCategoryThumbCard:FC<JobCategoryThumbCardProps> = ({logo, title, url}) => {

    return (
        <Link href={url} className="border border-gray-200 rounded-lg flex flex-col justify-center items-center p-4">
            {logo}
            <Typography align="center" variant="small" className="!font-bold">
                {title}
            </Typography>
        </Link>
    );
};

export default JobCategoryThumbCard;

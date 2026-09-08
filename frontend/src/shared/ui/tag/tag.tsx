import {FC, ReactNode} from "react";
import {Typography} from "@/shared/ui/typography";

interface TagProps {
    children: ReactNode
}

const Tag:FC<TagProps> = ({children}) => {

    return (
        <div className="rounded-md border border-gray-200 bg-white px-3">
            <Typography tone="muted" variant="caption">
                {children}
            </Typography>
        </div>
    );
};

export default Tag;

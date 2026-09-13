import {FC, ReactNode} from "react";
import {Typography} from "@/shared/ui/typography";
import classNames from "classnames";

interface TagProps {
    children: ReactNode,
    bgMode?: "muted" | "white"
}

const SearchTag:FC<TagProps> = ({children, bgMode = "white"}) => {

    return (
        <div className={classNames("rounded-md border border-gray-200 px-3", bgMode === "white" ? "bg-white" : "bg-slate-100")}>
            <Typography tone="muted" variant="caption">
                {children}
            </Typography>
        </div>
    );
};

export default SearchTag;

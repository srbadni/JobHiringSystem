import {Typography} from "@/shared/ui/typography";
import {ChevronLeftIcon} from "@/shared/ui/icons/ChevronLeftIcon";

interface BreadCrumbStep {
    title: string
}

interface BreadCrumbProps {
    steps: BreadCrumbStep[]
}

const BreadCrumb = ({steps}: BreadCrumbProps) => {

    return (
        <div className="flex">
            {
                steps.map(({title}, index) => {
                    const isLast = steps.length - 1 === index;
                    return (
                        <div key={index} className="flex items-center">
                            <Typography as="span" tone="muted" variant="caption">{title}</Typography>
                            {!isLast && <ChevronLeftIcon className="mx-2" color="text-muted" width={12} height={12}/>}
                        </div>
                    )
                })
            }
        </div>
    );
};

export default BreadCrumb;

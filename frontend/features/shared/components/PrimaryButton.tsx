import React, {ButtonHTMLAttributes, FC, ReactNode} from 'react';

interface PrimaryButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>{
    children: ReactNode
}

const PrimaryButton:FC<PrimaryButtonProps> = ({children, ...props}) => {
    return (
        <button {...props}>
            {children}
        </button>
    );
};

export default PrimaryButton;

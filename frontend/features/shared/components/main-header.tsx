import React, {FC} from 'react';
import {MenuIcon} from "@/features/shared/components/MenuIcon";
import {Typography} from "@/features/widgets/typography";

interface HeaderProps {

}

const Header:FC<HeaderProps> = ({}) => {
    return (
        <header className="p-2 bg-white flex items-center">
            <span>logo</span>
            <Typography className="ms-auto me-4">ورود / ثبت نام</Typography>
            <MenuIcon />
        </header>
    );
};

export default Header;

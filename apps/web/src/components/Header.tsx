import React from "react";

interface HeaderProps {
title: string;
}

const Header: React.FC<HeaderProps> = ({ title }) => {
return ( <header className="bg-orange-500 text-white shadow-md py-4"> <h1 className="text-3xl font-bold text-center">{title}</h1> </header>
);
};

export default Header;

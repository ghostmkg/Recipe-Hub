import React from "react";

interface FooterProps {
year: number;
}

const Footer: React.FC<FooterProps> = ({ year }) => {
return ( <footer className="bg-gray-900 text-gray-300 text-center py-4 mt-auto"> <p>© {year} Recipe Hub — Built with ❤️ using FastAPI & React.</p> </footer>
);
};

export default Footer;

import React from "react";

interface GreetUserProps {
name: string;
}

const GreetUser: React.FC<GreetUserProps> = ({ name }) => {
return ( <div className="text-center mt-6"> <h2 className="text-2xl font-semibold text-gray-800">Hello, {name}! 👋</h2> <p className="text-gray-600 mt-2">
Welcome to <span className="text-orange-500 font-medium">Recipe Hub</span> — your place to explore, share, and
create delicious recipes. </p> </div>
);
};

export default GreetUser;

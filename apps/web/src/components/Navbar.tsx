import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-green-600 text-white p-4 flex justify-between items-center shadow-md">
      <Link to="/" className="font-bold text-xl">🍲 Open Recipe Hub</Link>
      <div className="space-x-4">
        <Link to="/" className="hover:underline">Home</Link>
        <Link to="/submit" className="hover:underline">Submit Recipe</Link>
      </div>
    </nav>
  );
}

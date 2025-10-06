import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import RecipeDetail from "./pages/RecipeDetail";
import SubmitRecipe from "./pages/SubmitRecipe";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50 text-gray-900">
        <nav className="bg-white shadow mb-6 p-4 flex justify-between">
          <Link to="/" className="text-xl font-bold text-blue-600">🍳 Recipe Hub</Link>
          <div className="space-x-4">
            <Link to="/" className="hover:text-blue-500">Home</Link>
            <Link to="/submit" className="hover:text-blue-500">Submit Recipe</Link>
          </div>
        </nav>

        <div className="max-w-4xl mx-auto p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/recipes/:id" element={<RecipeDetail />} />
            <Route path="/submit" element={<SubmitRecipe />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

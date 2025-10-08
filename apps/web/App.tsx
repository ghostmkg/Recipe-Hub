import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import Recipes from "./pages/Recipes";
import Users from "./pages/Users";
import Ratings from "./pages/Ratings";
import "./styles/style.css";

const App: React.FC = () => {
  return (
    <Router>
      <div className="app-container">
        <header className="app-header">
          <h1>🍲 Recipe Hub</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/recipes">Recipes</Link>
            <Link to="/users">Users</Link>
            <Link to="/ratings">Ratings</Link>
          </nav>
        </header>

        <main className="app-main">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/recipes" element={<Recipes />} />
            <Route path="/users" element={<Users />} />
            <Route path="/ratings" element={<Ratings />} />
          </Routes>
        </main>

        <footer className="app-footer">
          <p>© 2025 Recipe Hub. Built with ❤️ and FastAPI + React.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;

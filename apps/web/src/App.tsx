import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import SubmitRecipe from "./pages/SubmitRecipe";
import RecipeDetail from "./pages/RecipeDetail";

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Navbar />
        <main className="flex-grow container mx-auto mt-6 px-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/submit" element={<SubmitRecipe />} />
            <Route path="/recipes/:id" element={<RecipeDetail />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;

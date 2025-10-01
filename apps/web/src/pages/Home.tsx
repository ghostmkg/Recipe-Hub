import { useEffect, useState } from "react";
import RecipeCard from "../components/RecipeCard";
import SearchBar from "../components/SearchBar";
import { getRecipes } from "../lib/api";

interface Recipe {
  id: number;
  title: string;
  description: string;
  image?: string;
}

export default function Home() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [filtered, setFiltered] = useState<Recipe[]>([]);

  useEffect(() => {
    async function fetchRecipes() {
      const data = await getRecipes();
      setRecipes(data);
      setFiltered(data);
    }
    fetchRecipes();
  }, []);

  const handleSearch = (query: string) => {
    setFiltered(
      recipes.filter((r) =>
        r.title.toLowerCase().includes(query.toLowerCase())
      )
    );
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">🍲 Open Recipe Hub</h1>
      <SearchBar onSearch={handleSearch} />
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {filtered.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} />
        ))}
      </div>
    </div>
  );
}

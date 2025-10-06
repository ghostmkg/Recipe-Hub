import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { Recipe } from "../types/recipe";

export default function RecipeDetail() {
  const { id } = useParams<{ id: string }>();
  const [recipe, setRecipe] = useState<Recipe | null>(null);

  useEffect(() => {
    if (!id) return;
    axios.get<Recipe>(`http://localhost:8000/recipes/${id}`)
      .then((res) => setRecipe(res.data))
      .catch((err) => console.error(err));
  }, [id]);

  if (!recipe) return <p>Loading...</p>;

  return (
    <div className="border p-6 rounded shadow bg-white max-w-3xl mx-auto">
      <h2 className="text-3xl font-bold mb-4">{recipe.title}</h2>

      {recipe.image && (
        <img
          src={recipe.image.startsWith("http") ? recipe.image : `http://localhost:8000${recipe.image}`}
          alt={recipe.title}
          className="mb-4 w-full h-64 object-cover rounded"
        />
      )}

      <p className="mb-4">{recipe.description}</p>

      <h3 className="font-semibold mb-2">Ingredients</h3>
      <pre className="bg-gray-100 p-3 rounded mb-4 whitespace-pre-wrap">{recipe.ingredients}</pre>

      <h3 className="font-semibold mb-2">Steps</h3>
      <pre className="bg-gray-100 p-3 rounded whitespace-pre-wrap">{recipe.steps}</pre>
    </div>
  );
}

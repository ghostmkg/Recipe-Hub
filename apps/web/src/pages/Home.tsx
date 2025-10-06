import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { Recipe } from "../types/recipe";

export default function Home() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);

  useEffect(() => {
    axios.get<Recipe[]>("http://localhost:8000/recipes")
      .then((res) => setRecipes(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-6">Latest Recipes</h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {recipes.map((r) => (
          <li key={r.id} className="border rounded shadow bg-white overflow-hidden">
            {r.image && (
              <img
                src={r.image.startsWith("http") ? r.image : `http://localhost:8000${r.image}`}
                alt={r.title}
                className="w-full h-48 object-cover"
              />
            )}
            <div className="p-4">
              <Link to={`/recipes/${r.id}`}>
                <h3 className="text-xl font-semibold text-blue-600 hover:underline">{r.title}</h3>
              </Link>
              <p className="text-gray-700 mt-2">{r.description}</p>
              {r.tags && (
                <div className="flex flex-wrap mt-3 gap-2">
                  {r.tags.split(",").map((tag) => (
                    <span
                      key={tag}
                      className="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-1 rounded-full"
                    >
                      {tag.trim()}
                    </span>
                  ))}
                </div>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

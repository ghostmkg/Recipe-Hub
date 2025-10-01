import { Link } from "react-router-dom";

interface RecipeCardProps {
  recipe: {
    id: number;
    title: string;
    description: string;
    image?: string;
  };
}

export default function RecipeCard({ recipe }: RecipeCardProps) {
  return (
    <div className="bg-white shadow-md rounded-lg p-4 hover:shadow-xl transition">
      <img
        src={recipe.image || "https://via.placeholder.com/300"}
        alt={recipe.title}
        className="w-full h-40 object-cover rounded-md"
      />
      <h2 className="text-xl font-semibold mt-3">{recipe.title}</h2>
      <p className="text-gray-600 mt-2 line-clamp-2">{recipe.description}</p>
      <Link
        to={`/recipes/${recipe.id}`}
        className="text-green-600 font-medium mt-3 inline-block"
      >
        View Details →
      </Link>
    </div>
  );
}

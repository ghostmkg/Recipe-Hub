import { useParams } from "react-router-dom";

export default function RecipeDetail() {
  const { id } = useParams();

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Recipe Details (ID: {id})</h1>
      <p className="text-gray-600">Full recipe details coming soon 🍴</p>
    </div>
  );
}

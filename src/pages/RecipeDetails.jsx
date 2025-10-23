sx
import { useEffect, useState } from "react";
import MediaCarousel from "../components/MediaCarousel";

export default function RecipeDetails({ recipeId }) {
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    fetch(`/api/recipes/${recipeId}`)
      .then((res) => res.json())
      .then((data) => setRecipe(data))
      .catch((err) => console.error(err));
  }, [recipeId]);

  if (!recipe) return <p>Loading recipe...</p>;

  return (
    <div className="recipe-details">
      <h1>{recipe.title}</h1>
      <p>{recipe.description}</p>

      <MediaCarousel media={recipe.media || []} />

      <h3>Ingredients</h3>
      <ul>
        {recipe.ingredients.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      <h3>Instructions</h3>
      <p>{recipe.instructions}</p>
    </div>
  );
}

import React, { useState } from 'react';
import SearchBar from '../components/SearchBar';
import RecipeCard from '../components/RecipeCard';
import RatingStars from '../components/RatingStars';
import { RecipeWithDetails, SearchFilters } from '../lib/types';

const Home: React.FC = () => {
  const [searchResults, setSearchResults] = useState<RecipeWithDetails[]>([]);
  const [searchFilters, setSearchFilters] = useState<SearchFilters>({});
  const [userRating, setUserRating] = useState<number>(0);

  // Sample recipe data for demonstration
  const sampleRecipes: RecipeWithDetails[] = [
    {
      id: 1,
      title: "Classic Spaghetti Carbonara",
      description: "A traditional Italian pasta dish with eggs, cheese, and pancetta. Creamy and delicious!",
      ingredients: ["400g spaghetti", "200g pancetta", "4 large eggs", "100g pecorino cheese", "black pepper", "salt"],
      steps: ["Cook pasta", "Fry pancetta", "Mix eggs and cheese", "Combine everything"],
      tags: ["Italian", "Pasta", "Quick", "Comfort Food"],
      image_url: "https://images.unsplash.com/photo-1621996346565-e3dbc353d946?w=400",
      created_by: 1,
      created_at: "2024-01-15T10:30:00Z",
      difficulty: "Medium",
      prep_time: 15,
      cook_time: 20,
      servings: 4,
      category: "Main Course",
      author: {
        id: 1,
        username: "ChefMarco",
        email: "marco@example.com",
        joined_at: "2023-12-01T00:00:00Z"
      },
      average_rating: 4.5,
      total_ratings: 128
    },
    {
      id: 2,
      title: "Chocolate Chip Cookies",
      description: "Soft and chewy chocolate chip cookies that are perfect for any occasion.",
      ingredients: ["2 cups flour", "1 cup butter", "3/4 cup brown sugar", "1/2 cup white sugar", "2 eggs", "2 cups chocolate chips"],
      steps: ["Mix dry ingredients", "Cream butter and sugars", "Add eggs and vanilla", "Mix in flour", "Add chocolate chips", "Bake"],
      tags: ["Dessert", "Cookies", "Chocolate", "Baking"],
      image_url: "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400",
      created_by: 2,
      created_at: "2024-01-10T14:20:00Z",
      difficulty: "Easy",
      prep_time: 20,
      cook_time: 12,
      servings: 24,
      category: "Dessert",
      author: {
        id: 2,
        username: "BakerSarah",
        email: "sarah@example.com",
        joined_at: "2023-11-15T00:00:00Z"
      },
      average_rating: 4.8,
      total_ratings: 95
    },
    {
      id: 3,
      title: "Mediterranean Quinoa Bowl",
      description: "A healthy and nutritious bowl packed with Mediterranean flavors and fresh vegetables.",
      ingredients: ["1 cup quinoa", "cherry tomatoes", "cucumber", "red onion", "feta cheese", "olives", "olive oil", "lemon juice"],
      steps: ["Cook quinoa", "Chop vegetables", "Prepare dressing", "Combine everything", "Top with feta"],
      tags: ["Healthy", "Mediterranean", "Vegetarian", "Lunch"],
      image_url: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400",
      created_by: 3,
      created_at: "2024-01-08T09:15:00Z",
      difficulty: "Easy",
      prep_time: 25,
      cook_time: 15,
      servings: 2,
      category: "Lunch",
      author: {
        id: 3,
        username: "HealthyEats",
        email: "healthy@example.com",
        joined_at: "2023-10-20T00:00:00Z"
      },
      average_rating: 4.2,
      total_ratings: 67
    }
  ];

  const handleSearch = (filters: SearchFilters) => {
    setSearchFilters(filters);
    // In a real app, this would make an API call
    console.log('Search filters:', filters);
    
    // Simulate search results
    let results = [...sampleRecipes];
    
    if (filters.query) {
      results = results.filter(recipe => 
        recipe.title.toLowerCase().includes(filters.query!.toLowerCase()) ||
        recipe.description.toLowerCase().includes(filters.query!.toLowerCase()) ||
        recipe.tags.some(tag => tag.toLowerCase().includes(filters.query!.toLowerCase()))
      );
    }
    
    if (filters.category) {
      results = results.filter(recipe => recipe.category === filters.category);
    }
    
    if (filters.difficulty) {
      results = results.filter(recipe => recipe.difficulty === filters.difficulty);
    }
    
    if (filters.max_prep_time) {
      results = results.filter(recipe => recipe.prep_time <= filters.max_prep_time!);
    }
    
    setSearchResults(results);
  };

  const handleClearSearch = () => {
    setSearchResults([]);
    setSearchFilters({});
  };

  const handleRecipeClick = (recipe: RecipeWithDetails) => {
    console.log('Recipe clicked:', recipe);
    // In a real app, this would navigate to recipe detail page
    alert(`Opening recipe: ${recipe.title}`);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <h1 className="text-3xl font-bold text-gray-900 text-center">
            🍲 Recipe Hub
          </h1>
          <p className="text-center text-gray-600 mt-2">
            Discover, share, and rate amazing recipes from around the world
          </p>
        </div>
      </header>

      {/* Search Section */}
      <section className="py-8 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <SearchBar 
            onSearch={handleSearch}
            onClear={handleClearSearch}
            placeholder="Search for recipes, ingredients, or cuisines..."
          />
        </div>
      </section>

      {/* Rating Demo Section */}
      <section className="py-8 bg-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h2 className="text-xl font-semibold mb-4">Interactive Rating Demo</h2>
            <p className="text-gray-600 mb-4">Try rating this recipe:</p>
            <div className="flex items-center gap-4">
              <RatingStars 
                rating={userRating}
                interactive={true}
                onRatingChange={setUserRating}
                size="lg"
              />
              <span className="text-gray-600">
                {userRating > 0 ? `You rated: ${userRating}/5` : 'Click stars to rate'}
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* Recipe Grid */}
      <section className="py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {searchResults.length > 0 ? (
            <>
              <h2 className="text-2xl font-bold text-gray-900 mb-6">
                Search Results ({searchResults.length})
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {searchResults.map((recipe) => (
                  <RecipeCard
                    key={recipe.id}
                    recipe={recipe}
                    onClick={handleRecipeClick}
                  />
                ))}
              </div>
            </>
          ) : (
            <>
              <h2 className="text-2xl font-bold text-gray-900 mb-6">
                Featured Recipes
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {sampleRecipes.map((recipe) => (
                  <RecipeCard
                    key={recipe.id}
                    recipe={recipe}
                    onClick={handleRecipeClick}
                  />
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-gray-300">
            Made with ❤️ for Hacktoberfest 2025 by devvsaxena
          </p>
          <p className="text-sm text-gray-400 mt-2">
            Frontend components: RecipeCard, SearchBar, RatingStars
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
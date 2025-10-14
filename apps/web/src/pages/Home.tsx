import React, { useState, useEffect } from 'react'
import RecipeCard from '../components/RecipeCard'
import SearchBar from '../components/SearchBar'

interface Recipe {
  id: number
  title: string
  description: string
  prep_time: number
  cook_time: number
  difficulty: string
  image_url?: string
}

const Home: React.FC = () => {
  const [recipes, setRecipes] = useState<Recipe[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    fetchRecipes()
  }, [])

  const fetchRecipes = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/recipes')
      const data = await response.json()
      setRecipes(data.recipes || [])
    } catch (error) {
      console.error('Error fetching recipes:', error)
      // Use sample data if API fails
      setRecipes([
        {
          id: 1,
          title: "Delicious Pasta",
          description: "A simple and tasty pasta recipe that everyone will love",
          prep_time: 10,
          cook_time: 20,
          difficulty: "easy"
        },
        {
          id: 2,
          title: "Chocolate Cake",
          description: "Rich and moist chocolate cake perfect for celebrations",
          prep_time: 30,
          cook_time: 45,
          difficulty: "medium"
        },
        {
          id: 3,
          title: "Beef Stir Fry",
          description: "Quick and healthy beef stir fry with fresh vegetables",
          prep_time: 15,
          cook_time: 10,
          difficulty: "easy"
        }
      ])
    } finally {
      setLoading(false)
    }
  }

  const filteredRecipes = recipes.filter(recipe =>
    recipe.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    recipe.description.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <div className="px-4 py-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Welcome to Recipe Hub
          </h1>
          <p className="text-xl text-gray-600">
            Discover and share amazing recipes from around the world
          </p>
        </div>

        <div className="mb-8">
          <SearchBar 
            value={searchTerm}
            onChange={setSearchTerm}
            placeholder="Search recipes..."
          />
        </div>

        {loading ? (
          <div className="text-center py-8">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
            <p className="mt-2 text-gray-600">Loading recipes...</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredRecipes.length > 0 ? (
              filteredRecipes.map((recipe) => (
                <RecipeCard key={recipe.id} recipe={recipe} />
              ))
            ) : (
              <div className="col-span-full text-center py-8">
                <p className="text-gray-600 text-lg">
                  {searchTerm ? 'No recipes found matching your search.' : 'No recipes available yet.'}
                </p>
                <a 
                  href="/submit" 
                  className="mt-4 inline-block bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Submit the first recipe!
                </a>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

export default Home

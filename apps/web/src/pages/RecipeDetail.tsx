import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

interface Recipe {
  id: number
  title: string
  description: string
  ingredients: string[]
  instructions: string[]
  prep_time: number
  cook_time: number
  servings: number
  difficulty: string
  category: string
  image_url?: string
}

const RecipeDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>()
  const [recipe, setRecipe] = useState<Recipe | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (id) {
      fetchRecipe(parseInt(id))
    }
  }, [id])

  const fetchRecipe = async (recipeId: number) => {
    try {
      const response = await fetch(`http://localhost:8000/api/v1/recipes/${recipeId}`)
      const data = await response.json()
      setRecipe(data)
    } catch (error) {
      console.error('Error fetching recipe:', error)
      // Use sample data if API fails
      setRecipe({
        id: recipeId,
        title: "Delicious Pasta",
        description: "A simple and tasty pasta recipe that everyone will love",
        ingredients: ["Pasta", "Tomato sauce", "Cheese", "Herbs"],
        instructions: [
          "Boil water in a large pot",
          "Add pasta and cook according to package directions",
          "Heat tomato sauce in a separate pan",
          "Drain pasta and mix with sauce",
          "Serve with cheese and herbs"
        ],
        prep_time: 10,
        cook_time: 20,
        servings: 4,
        difficulty: "easy",
        category: "Main Course"
      })
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="text-center py-8">
        <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        <p className="mt-2 text-gray-600">Loading recipe...</p>
      </div>
    )
  }

  if (!recipe) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-600 text-lg">Recipe not found</p>
        <a href="/" className="mt-4 inline-block text-blue-600 hover:text-blue-800">
          ← Back to Home
        </a>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-6">
      <div className="bg-white rounded-lg shadow-lg overflow-hidden">
        {recipe.image_url && (
          <img 
            src={recipe.image_url} 
            alt={recipe.title}
            className="w-full h-64 object-cover"
          />
        )}
        
        <div className="p-6">
          <div className="flex justify-between items-start mb-4">
            <h1 className="text-3xl font-bold text-gray-900">{recipe.title}</h1>
            <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium">
              {recipe.difficulty}
            </span>
          </div>
          
          <p className="text-gray-600 mb-6">{recipe.description}</p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900">Prep Time</h3>
              <p className="text-gray-600">{recipe.prep_time} minutes</p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900">Cook Time</h3>
              <p className="text-gray-600">{recipe.cook_time} minutes</p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900">Servings</h3>
              <p className="text-gray-600">{recipe.servings} people</p>
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">Ingredients</h2>
              <ul className="space-y-2">
                {recipe.ingredients.map((ingredient, index) => (
                  <li key={index} className="flex items-center">
                    <span className="w-2 h-2 bg-blue-600 rounded-full mr-3"></span>
                    {ingredient}
                  </li>
                ))}
              </ul>
            </div>
            
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">Instructions</h2>
              <ol className="space-y-3">
                {recipe.instructions.map((instruction, index) => (
                  <li key={index} className="flex">
                    <span className="flex-shrink-0 w-6 h-6 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-medium mr-3">
                      {index + 1}
                    </span>
                    <span>{instruction}</span>
                  </li>
                ))}
              </ol>
            </div>
          </div>
        </div>
      </div>
      
      <div className="mt-6 text-center">
        <a 
          href="/" 
          className="inline-block bg-gray-600 text-white px-6 py-2 rounded-lg hover:bg-gray-700 transition-colors"
        >
          ← Back to Recipes
        </a>
      </div>
    </div>
  )
}

export default RecipeDetail

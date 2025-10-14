import React, { useState, useEffect } from 'react';
import { Calendar, Plus, ShoppingCart, PieChart, Edit, Trash2 } from 'lucide-react';

interface MealPlan {
  id: number;
  name: string;
  description?: string;
  start_date: string;
  end_date: string;
  is_public: boolean;
  planned_meals: PlannedMeal[];
}

interface PlannedMeal {
  id: number;
  recipe_id: number;
  meal_date: string;
  meal_type: 'breakfast' | 'lunch' | 'dinner' | 'snack';
  servings: number;
  notes?: string;
}

interface ShoppingList {
  id: number;
  name: string;
  items: ShoppingListItem[];
}

interface ShoppingListItem {
  id: number;
  ingredient_name: string;
  quantity?: string;
  unit?: string;
  category?: string;
  is_purchased: boolean;
  notes?: string;
}

interface NutritionSummary {
  total_calories: number;
  total_protein: number;
  total_carbs: number;
  total_fat: number;
  meals_count: number;
}

const MealPlannerDashboard: React.FC = () => {
  const [mealPlans, setMealPlans] = useState<MealPlan[]>([]);
  const [selectedPlan, setSelectedPlan] = useState<MealPlan | null>(null);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [shoppingList, setShoppingList] = useState<ShoppingList | null>(null);
  const [nutrition, setNutrition] = useState<NutritionSummary | null>(null);
  const [loading, setLoading] = useState(true);

  // Mock data for demonstration
  useEffect(() => {
    // In a real app, this would fetch from the API
    const mockMealPlans: MealPlan[] = [
      {
        id: 1,
        name: "Weekly Meal Plan",
        description: "Healthy meals for the week",
        start_date: "2024-10-01",
        end_date: "2024-10-07",
        is_public: false,
        planned_meals: [
          {
            id: 1,
            recipe_id: 1,
            meal_date: "2024-10-01",
            meal_type: "breakfast",
            servings: 2,
            notes: "Start the week healthy"
          },
          {
            id: 2,
            recipe_id: 2,
            meal_date: "2024-10-01",
            meal_type: "lunch",
            servings: 2
          }
        ]
      }
    ];
    
    setMealPlans(mockMealPlans);
    setSelectedPlan(mockMealPlans[0]);
    setLoading(false);
  }, []);

  const generateShoppingList = async (planId: number) => {
    // In a real app, this would call the API
    const mockShoppingList: ShoppingList = {
      id: 1,
      name: "Shopping List for Weekly Meal Plan",
      items: [
        {
          id: 1,
          ingredient_name: "Eggs",
          quantity: "12",
          unit: "pieces",
          category: "Dairy",
          is_purchased: false
        },
        {
          id: 2,
          ingredient_name: "Bread",
          quantity: "1",
          unit: "loaf",
          category: "Bakery",
          is_purchased: false
        },
        {
          id: 3,
          ingredient_name: "Chicken Breast",
          quantity: "2",
          unit: "lbs",
          category: "Meat",
          is_purchased: false
        }
      ]
    };
    
    setShoppingList(mockShoppingList);
  };

  const getNutritionSummary = async (planId: number) => {
    // In a real app, this would call the API
    const mockNutrition: NutritionSummary = {
      total_calories: 1800,
      total_protein: 120,
      total_carbs: 180,
      total_fat: 60,
      meals_count: 14
    };
    
    setNutrition(mockNutrition);
  };

  const toggleShoppingItem = (itemId: number) => {
    if (!shoppingList) return;
    
    setShoppingList({
      ...shoppingList,
      items: shoppingList.items.map(item =>
        item.id === itemId ? { ...item, is_purchased: !item.is_purchased } : item
      )
    });
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 flex items-center">
            <Calendar className="mr-3 text-blue-600" />
            Meal Planner
          </h1>
          <button
            onClick={() => setShowCreateForm(true)}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-blue-700 transition-colors"
          >
            <Plus className="mr-2" size={20} />
            New Meal Plan
          </button>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Meal Plans List */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-semibold mb-4">Your Meal Plans</h2>
              <div className="space-y-3">
                {mealPlans.map((plan) => (
                  <div
                    key={plan.id}
                    onClick={() => setSelectedPlan(plan)}
                    className={`p-4 rounded-lg cursor-pointer transition-colors ${
                      selectedPlan?.id === plan.id
                        ? 'bg-blue-50 border border-blue-200'
                        : 'bg-gray-50 hover:bg-gray-100'
                    }`}
                  >
                    <h3 className="font-medium">{plan.name}</h3>
                    <p className="text-sm text-gray-600">
                      {new Date(plan.start_date).toLocaleDateString()} - {new Date(plan.end_date).toLocaleDateString()}
                    </p>
                    <p className="text-sm text-gray-500">{plan.planned_meals.length} meals planned</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-2">
            {selectedPlan && (
              <div className="space-y-6">
                {/* Plan Details */}
                <div className="bg-white rounded-lg shadow-md p-6">
                  <div className="flex justify-between items-start mb-4">
                    <div>
                      <h2 className="text-2xl font-semibold">{selectedPlan.name}</h2>
                      <p className="text-gray-600">{selectedPlan.description}</p>
                    </div>
                    <div className="flex space-x-2">
                      <button className="p-2 text-gray-500 hover:text-blue-600">
                        <Edit size={20} />
                      </button>
                      <button className="p-2 text-gray-500 hover:text-red-600">
                        <Trash2 size={20} />
                      </button>
                    </div>
                  </div>
                  
                  <div className="flex space-x-4">
                    <button
                      onClick={() => generateShoppingList(selectedPlan.id)}
                      className="bg-green-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-green-700 transition-colors"
                    >
                      <ShoppingCart className="mr-2" size={20} />
                      Generate Shopping List
                    </button>
                    <button
                      onClick={() => getNutritionSummary(selectedPlan.id)}
                      className="bg-purple-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-purple-700 transition-colors"
                    >
                      <PieChart className="mr-2" size={20} />
                      Nutrition Summary
                    </button>
                  </div>
                </div>

                {/* Planned Meals */}
                <div className="bg-white rounded-lg shadow-md p-6">
                  <h3 className="text-xl font-semibold mb-4">Planned Meals</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {selectedPlan.planned_meals.map((meal) => (
                      <div key={meal.id} className="border rounded-lg p-4">
                        <div className="flex justify-between items-start mb-2">
                          <h4 className="font-medium capitalize">{meal.meal_type}</h4>
                          <span className="text-sm text-gray-500">
                            {new Date(meal.meal_date).toLocaleDateString()}
                          </span>
                        </div>
                        <p className="text-sm text-gray-600">Recipe ID: {meal.recipe_id}</p>
                        <p className="text-sm text-gray-600">Servings: {meal.servings}</p>
                        {meal.notes && (
                          <p className="text-sm text-gray-500 mt-2">{meal.notes}</p>
                        )}
                      </div>
                    ))}
                  </div>
                  <button className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-blue-700 transition-colors">
                    <Plus className="mr-2" size={16} />
                    Add Meal
                  </button>
                </div>

                {/* Shopping List */}
                {shoppingList && (
                  <div className="bg-white rounded-lg shadow-md p-6">
                    <h3 className="text-xl font-semibold mb-4">{shoppingList.name}</h3>
                    <div className="space-y-2">
                      {shoppingList.items.map((item) => (
                        <div
                          key={item.id}
                          className="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
                        >
                          <div className="flex items-center">
                            <input
                              type="checkbox"
                              checked={item.is_purchased}
                              onChange={() => toggleShoppingItem(item.id)}
                              className="mr-3"
                            />
                            <div className={item.is_purchased ? 'line-through text-gray-500' : ''}>
                              <span className="font-medium">{item.ingredient_name}</span>
                              {item.quantity && item.unit && (
                                <span className="text-sm text-gray-600 ml-2">
                                  {item.quantity} {item.unit}
                                </span>
                              )}
                            </div>
                          </div>
                          {item.category && (
                            <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full">
                              {item.category}
                            </span>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Nutrition Summary */}
                {nutrition && (
                  <div className="bg-white rounded-lg shadow-md p-6">
                    <h3 className="text-xl font-semibold mb-4">Nutrition Summary</h3>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{nutrition.total_calories}</div>
                        <div className="text-sm text-gray-600">Calories</div>
                      </div>
                      <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{nutrition.total_protein}g</div>
                        <div className="text-sm text-gray-600">Protein</div>
                      </div>
                      <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{nutrition.total_carbs}g</div>
                        <div className="text-sm text-gray-600">Carbs</div>
                      </div>
                      <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{nutrition.total_fat}g</div>
                        <div className="text-sm text-gray-600">Fat</div>
                      </div>
                    </div>
                    <div className="mt-4 text-center text-gray-600">
                      Based on {nutrition.meals_count} planned meals
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Create Meal Plan Modal */}
      {showCreateForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-md w-full mx-4">
            <h3 className="text-xl font-semibold mb-4">Create New Meal Plan</h3>
            <form className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Plan Name
                </label>
                <input
                  type="text"
                  className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Enter meal plan name"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Description
                </label>
                <textarea
                  className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  rows={3}
                  placeholder="Optional description"
                />
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Start Date
                  </label>
                  <input
                    type="date"
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    End Date
                  </label>
                  <input
                    type="date"
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>
              <div className="flex items-center">
                <input
                  type="checkbox"
                  id="isPublic"
                  className="mr-2"
                />
                <label htmlFor="isPublic" className="text-sm text-gray-700">
                  Make this meal plan public
                </label>
              </div>
              <div className="flex justify-end space-x-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowCreateForm(false)}
                  className="px-4 py-2 text-gray-600 hover:text-gray-800"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Create Plan
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default MealPlannerDashboard;
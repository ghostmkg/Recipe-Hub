// Meal Planning API types and functions
export interface MealPlan {
  id: number;
  name: string;
  description?: string;
  start_date: string;
  end_date: string;
  is_public: boolean;
  user_id: number;
  created_at: string;
  updated_at: string;
  planned_meals: PlannedMeal[];
}

export interface PlannedMeal {
  id: number;
  meal_plan_id: number;
  recipe_id: number;
  meal_date: string;
  meal_type: 'breakfast' | 'lunch' | 'dinner' | 'snack';
  servings: number;
  notes?: string;
  created_at: string;
}

export interface ShoppingList {
  id: number;
  meal_plan_id: number;
  name: string;
  created_at: string;
  updated_at: string;
  items: ShoppingListItem[];
}

export interface ShoppingListItem {
  id: number;
  shopping_list_id: number;
  ingredient_name: string;
  quantity?: string;
  unit?: string;
  category?: string;
  is_purchased: boolean;
  notes?: string;
}

export interface NutritionSummary {
  total_calories: number;
  total_protein: number;
  total_carbs: number;
  total_fat: number;
  meals_count: number;
}

export interface CreateMealPlanRequest {
  name: string;
  description?: string;
  start_date: string;
  end_date: string;
  is_public?: boolean;
}

export interface CreatePlannedMealRequest {
  recipe_id: number;
  meal_date: string;
  meal_type: 'breakfast' | 'lunch' | 'dinner' | 'snack';
  servings: number;
  notes?: string;
}

const API_BASE_URL = '/api/v1';

// Meal Plan API functions
export const mealPlanAPI = {
  // Create a new meal plan
  createMealPlan: async (data: CreateMealPlanRequest): Promise<MealPlan> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to create meal plan');
    }

    return response.json();
  },

  // Get all meal plans for the current user
  getMealPlans: async (skip: number = 0, limit: number = 100): Promise<MealPlan[]> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans?skip=${skip}&limit=${limit}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch meal plans');
    }

    return response.json();
  },

  // Get a specific meal plan
  getMealPlan: async (id: number): Promise<MealPlan> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${id}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch meal plan');
    }

    return response.json();
  },

  // Update a meal plan
  updateMealPlan: async (id: number, data: Partial<CreateMealPlanRequest>): Promise<MealPlan> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to update meal plan');
    }

    return response.json();
  },

  // Delete a meal plan
  deleteMealPlan: async (id: number): Promise<void> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to delete meal plan');
    }
  },

  // Add a planned meal to a meal plan
  addPlannedMeal: async (mealPlanId: number, data: CreatePlannedMealRequest): Promise<PlannedMeal> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${mealPlanId}/meals`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to add planned meal');
    }

    return response.json();
  },

  // Get planned meals for a meal plan
  getPlannedMeals: async (mealPlanId: number): Promise<PlannedMeal[]> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${mealPlanId}/meals`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch planned meals');
    }

    return response.json();
  },

  // Update a planned meal
  updatePlannedMeal: async (plannedMealId: number, data: Partial<CreatePlannedMealRequest>): Promise<PlannedMeal> => {
    const response = await fetch(`${API_BASE_URL}/planned-meals/${plannedMealId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to update planned meal');
    }

    return response.json();
  },

  // Delete a planned meal
  deletePlannedMeal: async (plannedMealId: number): Promise<void> => {
    const response = await fetch(`${API_BASE_URL}/planned-meals/${plannedMealId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to delete planned meal');
    }
  },

  // Generate shopping list from meal plan
  generateShoppingList: async (mealPlanId: number): Promise<ShoppingList> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${mealPlanId}/shopping-list`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to generate shopping list');
    }

    return response.json();
  },

  // Get shopping list for a meal plan
  getShoppingList: async (mealPlanId: number): Promise<ShoppingList> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${mealPlanId}/shopping-list`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch shopping list');
    }

    return response.json();
  },

  // Toggle shopping item purchased status
  toggleShoppingItem: async (itemId: number, isPurchased: boolean): Promise<void> => {
    const response = await fetch(`${API_BASE_URL}/shopping-items/${itemId}/purchase?is_purchased=${isPurchased}`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to update shopping item');
    }
  },

  // Get nutrition summary for a meal plan
  getNutritionSummary: async (mealPlanId: number): Promise<NutritionSummary> => {
    const response = await fetch(`${API_BASE_URL}/meal-plans/${mealPlanId}/nutrition`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch nutrition summary');
    }

    return response.json();
  },
};
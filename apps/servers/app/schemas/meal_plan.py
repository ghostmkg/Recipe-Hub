from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class MealType(str, Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class MealPlanBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    is_public: bool = False

class MealPlanCreate(MealPlanBase):
    pass

class MealPlanUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_public: Optional[bool] = None

class PlannedMealBase(BaseModel):
    recipe_id: int
    meal_date: datetime
    meal_type: MealType
    servings: int = Field(default=1, ge=1)
    notes: Optional[str] = None

class PlannedMealCreate(PlannedMealBase):
    pass

class PlannedMealUpdate(BaseModel):
    recipe_id: Optional[int] = None
    meal_date: Optional[datetime] = None
    meal_type: Optional[MealType] = None
    servings: Optional[int] = Field(None, ge=1)
    notes: Optional[str] = None

class PlannedMeal(PlannedMealBase):
    id: int
    meal_plan_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class MealPlan(MealPlanBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    planned_meals: List[PlannedMeal] = []
    
    class Config:
        from_attributes = True

class ShoppingListItemBase(BaseModel):
    ingredient_name: str = Field(..., min_length=1, max_length=200)
    quantity: Optional[str] = Field(None, max_length=100)
    unit: Optional[str] = Field(None, max_length=50)
    category: Optional[str] = Field(None, max_length=100)
    is_purchased: bool = False
    notes: Optional[str] = None

class ShoppingListItemCreate(ShoppingListItemBase):
    pass

class ShoppingListItemUpdate(BaseModel):
    ingredient_name: Optional[str] = Field(None, min_length=1, max_length=200)
    quantity: Optional[str] = Field(None, max_length=100)
    unit: Optional[str] = Field(None, max_length=50)
    category: Optional[str] = Field(None, max_length=100)
    is_purchased: Optional[bool] = None
    notes: Optional[str] = None

class ShoppingListItem(ShoppingListItemBase):
    id: int
    shopping_list_id: int
    
    class Config:
        from_attributes = True

class ShoppingListBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)

class ShoppingListCreate(ShoppingListBase):
    meal_plan_id: int

class ShoppingList(ShoppingListBase):
    id: int
    meal_plan_id: int
    created_at: datetime
    updated_at: datetime
    items: List[ShoppingListItem] = []
    
    class Config:
        from_attributes = True

class NutritionSummary(BaseModel):
    total_calories: float
    total_protein: float
    total_carbs: float
    total_fat: float
    meals_count: int
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.deps.auth import get_current_user
from app.core.database import get_db
from app.services.meal_plan_service import MealPlanService
from app.schemas.meal_plan import (
    MealPlan, MealPlanCreate, MealPlanUpdate,
    PlannedMeal, PlannedMealCreate, PlannedMealUpdate,
    ShoppingList, NutritionSummary
)
from app.schemas.user import User

router = APIRouter()

@router.post("/meal-plans", response_model=MealPlan, status_code=status.HTTP_201_CREATED)
async def create_meal_plan(
    meal_plan_data: MealPlanCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new meal plan"""
    service = MealPlanService(db)
    return service.create_meal_plan(meal_plan_data, current_user.id)

@router.get("/meal-plans", response_model=List[MealPlan])
async def get_meal_plans(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all meal plans for the current user"""
    service = MealPlanService(db)
    return service.get_meal_plans(current_user.id, skip, limit)

@router.get("/meal-plans/{meal_plan_id}", response_model=MealPlan)
async def get_meal_plan(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific meal plan"""
    service = MealPlanService(db)
    meal_plan = service.get_meal_plan(meal_plan_id, current_user.id)
    
    if not meal_plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )
    
    return meal_plan

@router.put("/meal-plans/{meal_plan_id}", response_model=MealPlan)
async def update_meal_plan(
    meal_plan_id: int,
    update_data: MealPlanUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a meal plan"""
    service = MealPlanService(db)
    meal_plan = service.update_meal_plan(meal_plan_id, current_user.id, update_data)
    
    if not meal_plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )
    
    return meal_plan

@router.delete("/meal-plans/{meal_plan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meal_plan(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a meal plan"""
    service = MealPlanService(db)
    success = service.delete_meal_plan(meal_plan_id, current_user.id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )

@router.post("/meal-plans/{meal_plan_id}/meals", response_model=PlannedMeal, status_code=status.HTTP_201_CREATED)
async def add_planned_meal(
    meal_plan_id: int,
    planned_meal_data: PlannedMealCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Add a meal to a meal plan"""
    service = MealPlanService(db)
    planned_meal = service.add_planned_meal(meal_plan_id, current_user.id, planned_meal_data)
    
    if not planned_meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )
    
    return planned_meal

@router.get("/meal-plans/{meal_plan_id}/meals", response_model=List[PlannedMeal])
async def get_planned_meals(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all planned meals for a meal plan"""
    service = MealPlanService(db)
    return service.get_planned_meals(meal_plan_id, current_user.id)

@router.put("/planned-meals/{planned_meal_id}", response_model=PlannedMeal)
async def update_planned_meal(
    planned_meal_id: int,
    update_data: PlannedMealUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a planned meal"""
    service = MealPlanService(db)
    planned_meal = service.update_planned_meal(planned_meal_id, current_user.id, update_data)
    
    if not planned_meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planned meal not found"
        )
    
    return planned_meal

@router.delete("/planned-meals/{planned_meal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_planned_meal(
    planned_meal_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a planned meal"""
    service = MealPlanService(db)
    success = service.delete_planned_meal(planned_meal_id, current_user.id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planned meal not found"
        )

@router.post("/meal-plans/{meal_plan_id}/shopping-list", response_model=ShoppingList, status_code=status.HTTP_201_CREATED)
async def generate_shopping_list(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate shopping list from meal plan"""
    service = MealPlanService(db)
    shopping_list = service.generate_shopping_list(meal_plan_id, current_user.id)
    
    if not shopping_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )
    
    return shopping_list

@router.get("/meal-plans/{meal_plan_id}/shopping-list", response_model=ShoppingList)
async def get_shopping_list(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get shopping list for a meal plan"""
    service = MealPlanService(db)
    shopping_list = service.get_shopping_list(meal_plan_id, current_user.id)
    
    if not shopping_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shopping list not found"
        )
    
    return shopping_list

@router.patch("/shopping-items/{item_id}/purchase")
async def toggle_shopping_item(
    item_id: int,
    is_purchased: bool,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mark shopping list item as purchased/unpurchased"""
    service = MealPlanService(db)
    item = service.update_shopping_item(item_id, current_user.id, is_purchased)
    
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shopping list item not found"
        )
    
    return {"message": "Item updated successfully"}

@router.get("/meal-plans/{meal_plan_id}/nutrition", response_model=NutritionSummary)
async def get_nutrition_summary(
    meal_plan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get nutrition summary for a meal plan"""
    service = MealPlanService(db)
    nutrition = service.get_nutrition_summary(meal_plan_id, current_user.id)
    
    if not nutrition:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found"
        )
    
    return nutrition
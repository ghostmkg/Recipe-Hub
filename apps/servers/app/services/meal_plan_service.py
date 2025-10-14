from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
from app.models.meal_plan import MealPlan, PlannedMeal, ShoppingList, ShoppingListItem
from app.schemas.meal_plan import (
    MealPlanCreate, MealPlanUpdate, PlannedMealCreate, PlannedMealUpdate,
    ShoppingListCreate, ShoppingListItemCreate, NutritionSummary
)

class MealPlanService:
    def __init__(self, db: Session):
        self.db = db

    def create_meal_plan(self, meal_plan_data: MealPlanCreate, user_id: int) -> MealPlan:
        """Create a new meal plan for a user"""
        meal_plan = MealPlan(
            **meal_plan_data.dict(),
            user_id=user_id
        )
        self.db.add(meal_plan)
        self.db.commit()
        self.db.refresh(meal_plan)
        return meal_plan

    def get_meal_plans(self, user_id: int, skip: int = 0, limit: int = 100) -> List[MealPlan]:
        """Get all meal plans for a user"""
        return self.db.query(MealPlan).filter(
            MealPlan.user_id == user_id
        ).offset(skip).limit(limit).all()

    def get_meal_plan(self, meal_plan_id: int, user_id: int) -> Optional[MealPlan]:
        """Get a specific meal plan by ID"""
        return self.db.query(MealPlan).filter(
            MealPlan.id == meal_plan_id,
            MealPlan.user_id == user_id
        ).first()

    def update_meal_plan(self, meal_plan_id: int, user_id: int, update_data: MealPlanUpdate) -> Optional[MealPlan]:
        """Update an existing meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return None
        
        update_dict = update_data.dict(exclude_unset=True)
        for field, value in update_dict.items():
            setattr(meal_plan, field, value)
        
        meal_plan.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(meal_plan)
        return meal_plan

    def delete_meal_plan(self, meal_plan_id: int, user_id: int) -> bool:
        """Delete a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return False
        
        self.db.delete(meal_plan)
        self.db.commit()
        return True

    def add_planned_meal(self, meal_plan_id: int, user_id: int, planned_meal_data: PlannedMealCreate) -> Optional[PlannedMeal]:
        """Add a meal to a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return None
        
        planned_meal = PlannedMeal(
            **planned_meal_data.dict(),
            meal_plan_id=meal_plan_id
        )
        self.db.add(planned_meal)
        self.db.commit()
        self.db.refresh(planned_meal)
        return planned_meal

    def get_planned_meals(self, meal_plan_id: int, user_id: int) -> List[PlannedMeal]:
        """Get all planned meals for a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return []
        
        return self.db.query(PlannedMeal).filter(
            PlannedMeal.meal_plan_id == meal_plan_id
        ).all()

    def update_planned_meal(self, planned_meal_id: int, user_id: int, update_data: PlannedMealUpdate) -> Optional[PlannedMeal]:
        """Update a planned meal"""
        planned_meal = self.db.query(PlannedMeal).join(MealPlan).filter(
            PlannedMeal.id == planned_meal_id,
            MealPlan.user_id == user_id
        ).first()
        
        if not planned_meal:
            return None
        
        update_dict = update_data.dict(exclude_unset=True)
        for field, value in update_dict.items():
            setattr(planned_meal, field, value)
        
        self.db.commit()
        self.db.refresh(planned_meal)
        return planned_meal

    def delete_planned_meal(self, planned_meal_id: int, user_id: int) -> bool:
        """Delete a planned meal"""
        planned_meal = self.db.query(PlannedMeal).join(MealPlan).filter(
            PlannedMeal.id == planned_meal_id,
            MealPlan.user_id == user_id
        ).first()
        
        if not planned_meal:
            return False
        
        self.db.delete(planned_meal)
        self.db.commit()
        return True

    def generate_shopping_list(self, meal_plan_id: int, user_id: int) -> Optional[ShoppingList]:
        """Generate a shopping list from a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return None
        
        # Check if shopping list already exists
        existing_list = self.db.query(ShoppingList).filter(
            ShoppingList.meal_plan_id == meal_plan_id
        ).first()
        
        if existing_list:
            # Delete existing items to regenerate
            self.db.query(ShoppingListItem).filter(
                ShoppingListItem.shopping_list_id == existing_list.id
            ).delete()
            shopping_list = existing_list
        else:
            # Create new shopping list
            shopping_list = ShoppingList(
                meal_plan_id=meal_plan_id,
                name=f"Shopping List for {meal_plan.name}"
            )
            self.db.add(shopping_list)
            self.db.commit()
            self.db.refresh(shopping_list)
        
        # Group ingredients by name and sum quantities
        ingredient_groups = {}
        
        for planned_meal in meal_plan.planned_meals:
            # This would need to be implemented based on your Recipe model
            # For now, we'll create sample ingredients
            sample_ingredients = [
                {"name": f"Ingredient for {planned_meal.recipe_id}", "quantity": f"{planned_meal.servings}", "unit": "servings", "category": "General"}
            ]
            
            for ingredient in sample_ingredients:
                name = ingredient["name"]
                if name in ingredient_groups:
                    # Simple quantity addition (in real implementation, this would be more sophisticated)
                    current_qty = int(ingredient_groups[name]["quantity"])
                    new_qty = int(ingredient["quantity"])
                    ingredient_groups[name]["quantity"] = str(current_qty + new_qty)
                else:
                    ingredient_groups[name] = ingredient
        
        # Create shopping list items
        for ingredient_name, ingredient_data in ingredient_groups.items():
            item = ShoppingListItem(
                shopping_list_id=shopping_list.id,
                ingredient_name=ingredient_name,
                quantity=ingredient_data["quantity"],
                unit=ingredient_data["unit"],
                category=ingredient_data["category"]
            )
            self.db.add(item)
        
        self.db.commit()
        self.db.refresh(shopping_list)
        return shopping_list

    def get_shopping_list(self, meal_plan_id: int, user_id: int) -> Optional[ShoppingList]:
        """Get shopping list for a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return None
        
        return self.db.query(ShoppingList).filter(
            ShoppingList.meal_plan_id == meal_plan_id
        ).first()

    def update_shopping_item(self, item_id: int, user_id: int, is_purchased: bool) -> Optional[ShoppingListItem]:
        """Mark a shopping list item as purchased/unpurchased"""
        item = self.db.query(ShoppingListItem).join(ShoppingList).join(MealPlan).filter(
            ShoppingListItem.id == item_id,
            MealPlan.user_id == user_id
        ).first()
        
        if not item:
            return None
        
        item.is_purchased = is_purchased
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_nutrition_summary(self, meal_plan_id: int, user_id: int) -> Optional[NutritionSummary]:
        """Get nutrition summary for a meal plan"""
        meal_plan = self.get_meal_plan(meal_plan_id, user_id)
        if not meal_plan:
            return None
        
        # This would calculate actual nutrition based on recipes
        # For now, returning mock data
        total_meals = len(meal_plan.planned_meals)
        
        return NutritionSummary(
            total_calories=total_meals * 350,  # Mock calculation
            total_protein=total_meals * 25,
            total_carbs=total_meals * 45,
            total_fat=total_meals * 15,
            meals_count=total_meals
        )
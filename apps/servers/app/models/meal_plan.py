from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class MealPlan(Base):
    __tablename__ = "meal_plans"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    is_public = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="meal_plans")
    planned_meals = relationship("PlannedMeal", back_populates="meal_plan", cascade="all, delete-orphan")

class PlannedMeal(Base):
    __tablename__ = "planned_meals"
    
    id = Column(Integer, primary_key=True, index=True)
    meal_plan_id = Column(Integer, ForeignKey("meal_plans.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    meal_date = Column(DateTime, nullable=False)
    meal_type = Column(String(50), nullable=False)  # breakfast, lunch, dinner, snack
    servings = Column(Integer, default=1)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    meal_plan = relationship("MealPlan", back_populates="planned_meals")
    recipe = relationship("Recipe", back_populates="planned_meals")

class ShoppingList(Base):
    __tablename__ = "shopping_lists"
    
    id = Column(Integer, primary_key=True, index=True)
    meal_plan_id = Column(Integer, ForeignKey("meal_plans.id"), nullable=False)
    name = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    meal_plan = relationship("MealPlan")
    items = relationship("ShoppingListItem", back_populates="shopping_list", cascade="all, delete-orphan")

class ShoppingListItem(Base):
    __tablename__ = "shopping_list_items"
    
    id = Column(Integer, primary_key=True, index=True)
    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=False)
    ingredient_name = Column(String(200), nullable=False)
    quantity = Column(String(100))  # e.g., "2 cups", "3 lbs", "1 piece"
    unit = Column(String(50))
    category = Column(String(100))  # e.g., "Produce", "Dairy", "Meat"
    is_purchased = Column(Boolean, default=False)
    notes = Column(Text)
    
    # Relationships
    shopping_list = relationship("ShoppingList", back_populates="items")
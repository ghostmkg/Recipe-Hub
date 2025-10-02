from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from apps.servers.app.core.database import get_db
from apps.servers.app.models.recipe import Recipe
from apps.servers.app.schemas.recipe import RecipeCreate, RecipeResponse

router = APIRouter()

# Create a recipe
@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        ingredients=recipe.ingredients,
        steps=recipe.steps,
        category=recipe.category,
        created_by=recipe.created_by
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Get all recipes (with optional category filter)
@router.get("/recipes", response_model=List[RecipeResponse])
def get_recipes(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Recipe)
    if category:
        query = query.filter(Recipe.category == category)
    return query.all()

# Get a single recipe by ID
@router.get("/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

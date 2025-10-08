from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models import recipe as recipe_model
from app.schemas import recipe as recipe_schema
from app.deps.auth import get_current_user

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/recipes", response_model=List[recipe_schema.RecipeRead], summary="List all recipes")
def list_recipes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    """
    Fetch a paginated list of recipes.
    """
    recipes = db.query(recipe_model.Recipe).offset(skip).limit(limit).all()
    return recipes


@router.get("/recipes/{recipe_id}", response_model=recipe_schema.RecipeRead, summary="Get a recipe by ID")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single recipe by its ID.
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("/recipes", response_model=recipe_schema.RecipeRead, status_code=status.HTTP_201_CREATED, summary="Create a new recipe")
def create_recipe(payload: recipe_schema.RecipeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Create a new recipe associated with the authenticated user.
    """
    new_recipe = recipe_model.Recipe(**payload.dict(), owner_id=current_user.id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe


@router.put("/recipes/{recipe_id}", response_model=recipe_schema.RecipeRead, summary="Update a recipe")
def update_recipe(recipe_id: int, payload: recipe_schema.RecipeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Update an existing recipe (only by its owner).
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if recipe.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this recipe")

    for key, value in payload.dict().items():
        setattr(recipe, key, value)

    db.commit()
    db.refresh(recipe)
    return recipe


@router.delete("/recipes/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a recipe")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Delete a recipe (only by its owner).
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if recipe.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this recipe")

    db.delete(recipe)
    db.commit()
    return {"detail": "Recipe deleted successfully"}

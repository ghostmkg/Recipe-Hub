from sqlalchemy.orm import Session
from apps.api import models, schemas
from datetime import datetime

# ---------------- Recipe CRUD ----------------
def create_recipe(db: Session, recipe: schemas.RecipeCreate, user_id: int = None, image_path: str = None):
    db_recipe = models.Recipe(
        title=recipe.title,
        description=recipe.description,
        ingredients=recipe.ingredients,
        steps=recipe.steps,
        tags=recipe.tags,
        image=image_path,
        created_by=user_id,
        created_at=datetime.utcnow()
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def list_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

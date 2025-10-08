
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models import rating as rating_model, recipe as recipe_model
from app.schemas import rating as rating_schema
from app.deps.auth import get_current_user

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/ratings/{recipe_id}", response_model=List[rating_schema.RatingRead], summary="Get all ratings for a recipe")
def get_ratings(recipe_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all ratings for a given recipe.
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    ratings = db.query(rating_model.Rating).filter(rating_model.Rating.recipe_id == recipe_id).all()
    return ratings


@router.post("/ratings/{recipe_id}", response_model=rating_schema.RatingRead, status_code=status.HTTP_201_CREATED, summary="Add or update a rating for a recipe")
def add_or_update_rating(recipe_id: int, payload: rating_schema.RatingCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Create or update a rating for a specific recipe by the authenticated user.
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    existing_rating = (
        db.query(rating_model.Rating)
        .filter(
            rating_model.Rating.recipe_id == recipe_id,
            rating_model.Rating.user_id == current_user.id
        )
        .first()
    )

    if existing_rating:
        existing_rating.score = payload.score
        existing_rating.comment = payload.comment
    else:
        new_rating = rating_model.Rating(
            recipe_id=recipe_id,
            user_id=current_user.id,
            score=payload.score,
            comment=payload.comment
        )
        db.add(new_rating)

    db.commit()
    db.refresh(recipe)
    return existing_rating or new_rating


@router.get("/ratings/{recipe_id}/average", summary="Get average rating for a recipe")
def get_average_rating(recipe_id: int, db: Session = Depends(get_db)):
    """
    Calculate and return the average rating score for a recipe.
    """
    recipe = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    ratings = db.query(rating_model.Rating).filter(rating_model.Rating.recipe_id == recipe_id).all()
    if not ratings:
        return {"recipe_id": recipe_id, "average_rating": None, "count": 0}

    avg = sum(r.score for r in ratings) / len(ratings)
    return {"recipe_id": recipe_id, "average_rating": round(avg, 2), "count": len(ratings)}

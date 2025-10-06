# apps/api/routers/ratings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RatingOut)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    # simple flow: assume user_id == 1 for demo; replace with auth-provided user id
    user_id = 1
    db_recipe = crud.get_recipe(db, rating.recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return crud.create_rating(db, rating, user_id)

@router.get("/recipe/{recipe_id}", response_model=List[schemas.RatingOut])
def get_ratings(recipe_id: int, db: Session = Depends(get_db)):
    return crud.get_ratings_for_recipe(db, recipe_id)

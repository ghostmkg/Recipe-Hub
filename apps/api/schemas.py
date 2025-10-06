# apps/api/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -----------------------
# User Schemas
# -----------------------
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    joined_at: datetime  # keep as datetime

    class Config:
        from_attributes = True  # Pydantic V2 replacement for orm_mode

# -----------------------
# Recipe Schemas
# -----------------------
class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: str
    steps: str
    tags: Optional[str] = None
    image: Optional[str] = None

class RecipeCreate(RecipeBase):
    pass

class RecipeOut(RecipeBase):
    id: int
    created_by: Optional[int]
    created_at: datetime  # keep as datetime

    class Config:
        from_attributes = True

# -----------------------
# Rating Schemas
# -----------------------
class RatingBase(BaseModel):
    recipe_id: int
    stars: int
    comment: Optional[str] = None

class RatingCreate(RatingBase):
    pass

class RatingOut(RatingBase):
    id: int
    user_id: int
    timestamp: datetime  # keep as datetime

    class Config:
        from_attributes = True

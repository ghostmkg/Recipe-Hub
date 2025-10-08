from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared properties
class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: Optional[str] = None
    instructions: Optional[str] = None
    image_url: Optional[str] = None


# Schema for creating a recipe
class RecipeCreate(RecipeBase):
    pass


# Schema for reading a recipe (from DB)
class RecipeRead(RecipeBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

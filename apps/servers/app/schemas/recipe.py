from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared properties
class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: str
    steps: str
    category: Optional[str] = None   # category added
    created_by: Optional[str] = None

# For creating a recipe
class RecipeCreate(RecipeBase):
    pass

# For updating a recipe
class RecipeUpdate(RecipeBase):
    pass

# Response schema
class RecipeResponse(RecipeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # for ORM compatibility

from pydantic import BaseModel, conint
from typing import Optional
from datetime import datetime


# Shared properties
class RatingBase(BaseModel):
    score: conint(ge=1, le=5)  # Rating between 1 and 5
    comment: Optional[str] = None


# Schema for creating or updating a rating
class RatingCreate(RatingBase):
    pass


# Schema for reading a rating (from DB)
class RatingRead(RatingBase):
    id: int
    recipe_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

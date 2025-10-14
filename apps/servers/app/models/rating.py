from sqlalchemy import Column, Integer, ForeignKey, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base import Base

class Rating(Base):
    __tablename__ = "ratings"
    __table_args__ = (UniqueConstraint("user_id", "recipe_id", name="user_recipe_unique"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    rating = Column(Float, nullable=False)

    user = relationship("User", backref="ratings")
    recipe = relationship("Recipe", backref="ratings")

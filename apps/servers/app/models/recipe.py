from sqlalchemy import Column, Integer, String, Text, DateTime, func
from apps.servers.app.core.database import Base
  
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    ingredients = Column(Text, nullable=False)
    steps = Column(Text, nullable=False)
    category = Column(String(100), nullable=True)  #category field
    created_by = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

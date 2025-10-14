from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql import func

Base = declarative_base()

class BaseModel(Base):
    """
    Base model class with common fields for all models
    """
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

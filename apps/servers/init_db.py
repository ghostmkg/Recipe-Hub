#!/usr/bin/env python3
"""
Database initialization script for Recipe Hub
"""

import sys
import os

# Add the app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.core.database import engine
from app.models.base import Base
from app.models.user import User
# Import other models when they are created
# from app.models.recipe import Recipe
# from app.models.rating import Rating

def init_db():
    """Initialize the database by creating all tables"""
    print("Creating database tables...")
    
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        
        # Print created tables
        print("\nCreated tables:")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
            
    except Exception as e:
        print(f"❌ Error creating database tables: {e}")
        sys.exit(1)

if __name__ == "__main__":
    init_db()
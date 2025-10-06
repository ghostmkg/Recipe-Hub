# scripts/seed_db.py
from apps.api.database import SessionLocal, engine
from apps.api import models, crud, schemas
from apps.api.models import Base

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    # create admin user if not exists
    if not db.query(models.User).filter(models.User.username == "admin").first():
        user = schemas.UserCreate(username="admin", email="admin@example.com", password="password")
        crud.create_user(db, user)
    # sample recipe
    if not db.query(models.Recipe).first():
        r = schemas.RecipeCreate(
            title="Sample Pancakes",
            description="Delicious sample pancakes for demo",
            ingredients="Flour\nEggs\nMilk\nSalt\nSugar",
            steps="1. Mix ingredients\n2. Cook on skillet",
            tags="breakfast,dessert"
        )
        crud.create_recipe(db, r, user_id=1)
    db.close()
    print("Seeded DB")

if __name__ == "__main__":
    seed()

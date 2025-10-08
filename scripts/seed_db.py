import json
from app.core.database import SessionLocal
from app.models.recipe import Recipe

def seed_recipes():
with open("data/samples/sample_recipes.json", "r") as f:
recipes = json.load(f)

```
db = SessionLocal()
for r in recipes:
    db.add(Recipe(**r))
db.commit()
db.close()
```

if **name** == "**main**":
print("🌱 Seeding database with sample recipes...")
seed_recipes()
print("✅ Done!")

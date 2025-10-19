from fastapi import APIRouter, HTTPException

router = APIRouter()

# In-memory categories list (replace with DB in production)
categories = ["desserts", "vegan", "quick meals", "gluten-free"]

@router.get("/categories")
async def get_categories():
    return {"categories": categories}

@router.post("/categories")
async def add_category(category_name: str):
    if category_name.lower() in categories:
        raise HTTPException(status_code=400, detail="Category already exists.")
    categories.append(category_name.lower())
    return {"message": f"Category '{category_name}' added successfully.", "categories": categories}

@router.delete("/categories/{category_name}")
async def delete_category(category_name: str):
    if category_name.lower() not in categories:
        raise HTTPException(status_code=404, detail="Category not found.")
    categories.remove(category_name.lower())
    return {"message": f"Category '{category_name}' deleted successfully.", "categories": categories}

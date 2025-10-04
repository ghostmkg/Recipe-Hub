from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_recipes():
    return [{"id": 1, "name": "Pasta"}, {"id": 2, "name": "Pizza"}]
#  just a minimal setup will update the rest later
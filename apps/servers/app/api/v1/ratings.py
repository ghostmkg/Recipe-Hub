from fastapi import APIRouter

router = APIRouter()

@router.get("/ratings")
def get_ratings():
    return {"message": "Ratings endpoint works!"}

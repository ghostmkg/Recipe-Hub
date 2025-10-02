from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "List of users will go here"}

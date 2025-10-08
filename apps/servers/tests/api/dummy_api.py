"""
This is a dummy API file.

It serves as a placeholder to ensure the 'api' package is tracked
in version control (e.g., Git) even if no real API modules exist yet.

Once you add your actual API routes (like health, users, recipes, etc.),
you can safely remove this file.
"""

# Example placeholder route (optional)
from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy", tags=["dummy"])
def dummy_endpoint():
    return {"message": "This is a placeholder API endpoint."}

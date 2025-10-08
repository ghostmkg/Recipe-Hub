from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health", summary="Health Check", tags=["health"])
async def health_check():
    """
    Simple endpoint to verify the API is running.
    Returns current server timestamp and a success message.
    """
    return {
        "status": "ok",
        "message": "Recipe Hub API is healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

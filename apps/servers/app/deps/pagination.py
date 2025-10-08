from fastapi import Query
from typing import Optional


def pagination_params(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: Optional[int] = Query(10, ge=1, le=100, description="Number of items to return"),
):
    """
    Common pagination dependency.
    Use this in list endpoints to automatically handle 'skip' and 'limit' query params.
    """
    return {"skip": skip, "limit": limit}

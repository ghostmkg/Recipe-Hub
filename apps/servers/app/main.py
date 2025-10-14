from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.api.v1 import health, recipes, users, ratings, uploads, meal_plans
import time
import logging

app = FastAPI(title="Recipe Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logging
logger = logging.getLogger(__name__)

# Middleware for request timing and logging
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request processed in {process_time:.2f} seconds")
    return response

# Global exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(recipes.router, prefix="/api/v1", tags=["recipes"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(ratings.router, prefix="/api/v1", tags=["ratings"])
app.include_router(uploads.router, prefix="/api/v1", tags=["uploads"])
app.include_router(meal_plans.router, prefix="/api/v1", tags=["meal-plans"])

@app.get("/")
async def root():
    return {"message": "Recipe Hub API is running"}

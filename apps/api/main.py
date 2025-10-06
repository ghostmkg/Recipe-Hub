from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.database import engine
from apps.api import models
from apps.api.routers import recipes

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Open Recipe Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])

@app.get("/")
def root():
    return {"message": "Open Recipe Hub API running"}

import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from fastapi.responses import FileResponse
from pathlib import Path

from app.deps.auth import get_current_user
from app.core.config import settings

router = APIRouter()

# Define upload directory (e.g., backend/uploads)
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/uploads/image", summary="Upload an image file")
async def upload_image(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    """
    Upload an image file (for a recipe or profile picture).
    Returns the file URL after saving.
    """
    allowed_types = ["image/jpeg", "image/png", "image/jpg"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG allowed.")

    # Generate a unique filename
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = UPLOAD_DIR / filename

    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(await file.read())

    file_url = f"/api/v1/uploads/{filename}"
    return {"filename": filename, "url": file_url}


@router.get("/uploads/{filename}", response_class=FileResponse, summary="Retrieve uploaded file")
async def get_uploaded_file(filename: str):
    """
    Retrieve an uploaded image by filename.
    """
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)

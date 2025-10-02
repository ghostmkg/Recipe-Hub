from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@router.get("/uploads")
async def list_uploads():
    # For now, just return a dummy response
    return {"message": "Uploads endpoint works!"}

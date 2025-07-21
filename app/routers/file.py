from fastapi import APIRouter, UploadFile, File, HTTPException
from app.minio_client import upload_to_minio, download_from_minio

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_id = await upload_to_minio(file)
        return {"file_id": file_id, "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{file_id}")
def download_file(file_id: str):
    try:
        response = download_from_minio(file_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

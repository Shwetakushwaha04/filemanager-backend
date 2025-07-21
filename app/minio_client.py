from minio import Minio
from fastapi.responses import StreamingResponse
from uuid import uuid4
import os
from dotenv import load_dotenv
from fastapi import UploadFile
from io import BytesIO

load_dotenv()

minio_client = Minio(
    endpoint=os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

bucket_name = os.getenv("MINIO_BUCKET")

async def upload_to_minio(file: UploadFile):
    file_id = str(uuid4())
    content = await file.read()

    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    minio_client.put_object(
        bucket_name,
        file_id,
        data=BytesIO(content),
        length=len(content),
        content_type=file.content_type
    )

    return file_id

def download_from_minio(file_id: str):
    data = minio_client.get_object(bucket_name, file_id)
    return StreamingResponse(data, media_type="application/octet-stream")

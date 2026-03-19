from fastapi import APIRouter, UploadFile, File
import os
import shutil

from api.services.videoservice import process_video

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/uploads")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    video_name = file.filename.replace(".mp4", "")

    process_video(file_path, video_name)

    return {
        "message": "Video processed successfully",
        "video_name": video_name
    }
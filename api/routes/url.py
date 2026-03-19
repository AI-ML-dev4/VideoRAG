from fastapi import APIRouter
from pydantic import BaseModel
import os

from videoconverter.url_to_video import download_video
from api.services.videoservice import process_video

router = APIRouter()


class URLRequest(BaseModel):
    url: str


@router.post("/url")
def process_url(request: URLRequest):
    video_path = download_video(request.url)

    video_name = os.path.basename(video_path).replace(".mp4", "")

    process_video(video_path, video_name)

    return {
        "message": "URL video processed successfully",
        "video_name": video_name
    }
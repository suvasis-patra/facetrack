from fastapi import APIRouter,UploadFile,File,HTTPException

import uuid
import os

UPLOAD_DIR="/tmp/uploads"
MAX_FILE_SIZE=1024*1024*50
ALLOWED_TYPES = ["video/mp4", "video/webm"]
router=APIRouter()

@router.post("/v1/videos")
async def upload_video(file: UploadFile = File(...)):
    if not file.content_type or file.content_type not in ALLOWED_TYPES:
        raise HTTPException(400, detail="Unsupported video format")

    video_id = str(uuid.uuid4())

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if not file.filename:
       raise HTTPException(status_code=400, detail="Filename missing")

    ext = os.path.splitext(file.filename)[1]

    if not ext:
      raise HTTPException(status_code=400, detail="Invalid file extension")
    file_path = os.path.join(UPLOAD_DIR, f"{video_id}.{ext}")

    try:
        with open(file_path, "wb") as f:
            total_size = 0
            while chunk := await file.read(1024 * 1024):
                total_size += len(chunk)

                if total_size > MAX_FILE_SIZE:
                    raise HTTPException(400, detail="File too large")

                f.write(chunk)

    except Exception as e:
        print(e)
        raise HTTPException(500, detail="Failed to save file")

    return {
        "video_id": video_id,
        "status": "uploaded"
    }


@router.get("/v1/videos/{video_id}/stream")
def stream_video(video_id):
      return {"message":"stream video"}

@router.get("/v1/videos/{video_id}/roi")
def get_roi(video_id):
      return []
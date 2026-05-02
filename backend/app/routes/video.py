from fastapi import APIRouter

router=APIRouter()

@router.post("/v1/videos")
def upload_video():
      return {"message":"upload videos here"}


@router.get("/v1/videos/{video_id}/stream")
def stream_video(video_id):
      return {"message":"stream video"}

@router.get("/v1/videos/{video_id}/roi")
def get_roi(video_id):
      return []
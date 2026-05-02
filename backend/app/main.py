from fastapi import FastAPI

from app.routes import video

app = FastAPI()

app.include_router(video.router)

@app.get("/")
def read_root():
    return {"message": "Backend is running"}
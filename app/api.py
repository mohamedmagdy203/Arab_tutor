from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import FileResponse
from app.dubbing import process_video_with_translated_audio
import subprocess
import os
import shutil
import uuid

router = APIRouter()

@router.post("/dub")
async def dub_video(request: Request, file: UploadFile = File(...)):
    video_id = uuid.uuid4().hex
    temp_video_path = f"app/videos/input_{video_id}.mp4"
    output_video_path = f"app/videos/output_{video_id}.mp4"
    lip_sync_path = f"app/videos/lipsync_{video_id}.mp4"

    os.makedirs(os.path.dirname(temp_video_path), exist_ok=True)
    with open(temp_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_video_with_translated_audio(temp_video_path, output_video_path)

    command = [
        "conda", "run", "-n", "wave_env", "python", "wav2lip_runner.py",
        temp_video_path, result["output_path"], lip_sync_path
    ]
    wav2lip_result = subprocess.run(command, capture_output=True, text=True)

    if wav2lip_result.returncode != 0:
        return {
            "status": "error",
            "stderr": wav2lip_result.stderr
        }

    download_url = f"{request.base_url}download/{os.path.basename(lip_sync_path)}"

    return {
        "summary": result["summary"],
        "download_url": download_url
    }

@router.get("/download/{filename}")
def download_final_video(filename: str):
    file_path = os.path.join("app/videos", filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type="video/mp4")
    return {"error": "File not found"}

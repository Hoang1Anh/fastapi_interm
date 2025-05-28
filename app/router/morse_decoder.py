from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import os
from morse_audio_decoder.morse import MorseCode

router = APIRouter()
UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# API 1: Upload và giải mã luôn
@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported")

    file_id = str(uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        morse_code = MorseCode.from_wavfile(file_path)
        out = morse_code.decode()
        print(out)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Decode error: {str(e)}")

    return {"file_id": file_id, "decoded_text": out}


# API 2: Dùng file_id để giải mã lại
@router.get("/decode-audio/{file_id}")
def decode_audio(file_id: str):
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        morse_code = MorseCode.from_wavfile(file_path)
        out = morse_code.decode()
        print(out)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Decode error: {str(e)}")

    return {"file_id": file_id, "decoded_text": out}

import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import subprocess
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas, crud
from typing import List
from shutil import copyfileobj
from pathlib import Path



 

router = APIRouter(prefix="/files") #, tags=["Storage"]

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
AUDIO_EXTS = {".mp3", ".wav", ".flac"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload", response_model=schemas.FileOut,tags=["Storage"])
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    file_hash = crud.calculate_file_hash(contents)

    # Check if hash exists
    db_file = db.query(models.File).filter_by(hash=file_hash).first()
    if db_file:
        raise HTTPException(status_code=400, detail="File already exists")

    # Determine folder
    ext = os.path.splitext(file.filename)[1].lower()
    subfolder = "audio" if ext in AUDIO_EXTS else "others"
    save_path = os.path.join(UPLOAD_DIR, subfolder, file.filename)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(contents)

    new_file = models.File(
        filename=file.filename,
        hash=file_hash,
        content_type=file.content_type,
        size=len(contents),
        path=save_path
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file

@router.get("/", response_model=List[schemas.FileOut],tags=["add"])
def list_files(db: Session = Depends(get_db)):
    return db.query(models.File).all()

@router.get("/{file_id}", response_model=schemas.FileOut, tags=["age"])
def get_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(models.File).get(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file

@router.get("/download/{file_id}", tags=["Storage"])
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(models.File).get(file_id)
    if not file or not os.path.exists(file.path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file.path, filename=file.filename, media_type=file.content_type) 


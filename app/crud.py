# app/crud.py
from sqlalchemy.orm import Session
from . import models
import hashlib

def calculate_hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()

def save_file_info(db: Session, filename: str, content: bytes, content_type: str):
    file_hash = calculate_hash(content)
    file = models.AudioFile(
        filename=filename,
        hash=file_hash,
        content_type=content_type
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    return file
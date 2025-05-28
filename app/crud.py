from sqlalchemy.orm import Session
from . import models
import hashlib

def calculate_file_hash(file_data: bytes):
    return hashlib.sha256(file_data).hexdigest()


def get_file_by_hash(db: Session, file_hash: str):
    return db.query(models.File).filter_by(hash=file_hash).first()

def create_file(db: Session, file_data: dict):
    new_file = models.File(**file_data)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file

def get_file(db: Session, file_id: int):
    return db.query(models.File).get(file_id)

def list_files(db: Session):
    return db.query(models.File).all()
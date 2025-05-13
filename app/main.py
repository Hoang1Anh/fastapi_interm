import os
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, models, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    file_hash = crud.calculate_hash(content)

    if db.query(models.AudioFile).filter_by(hash=file_hash).first():
        raise HTTPException(status_code=400, detail="File đã tồn tại!")

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(content)

    file_entry = crud.save_file_info(db, file.filename, content, file.content_type)
    return {"message": "Upload thành công", "file_id": file_entry.id}
from sqlmodel import Session, select
from app.models.LoaiNguoiDung import LoaiNguoiDung
from app.schemas.LoaiNguoiDung import LoaiNguoiDungCreate, LoaiNguoiDungUpdate

def create_loai_nguoi_dung(db: Session, data: LoaiNguoiDungCreate):
    loai = LoaiNguoiDung(**data.dict())
    db.add(loai)
    db.commit()
    db.refresh(loai)
    return loai

def get_all_loai_nguoi_dung(db: Session):
    return db.exec(select(LoaiNguoiDung)).all()

def update_loai_nguoi_dung(db: Session, loai_id: int, data: LoaiNguoiDungUpdate):
    loai = db.get(LoaiNguoiDung, loai_id)
    if not loai:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(loai, key, value)
    db.add(loai)
    db.commit()
    db.refresh(loai)
    return loai

def delete_loai_nguoi_dung(db: Session, loai_id: int):
    loai = db.get(LoaiNguoiDung, loai_id)
    if not loai:
        return None
    db.delete(loai)
    db.commit()
    return True

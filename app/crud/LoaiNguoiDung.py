from sqlmodel import Session, select
from app.models.LoaiNguoiDung import LoaiNguoiDung
from app.schemas.LoaiNguoiDung import LoaiNguoiDungCreate, LoaiNguoiDungUpdate
from app import utils

def create_loai_nguoi_dung(db: Session, data: LoaiNguoiDungCreate):
    loai = LoaiNguoiDung(**data.dict())
    db.add(loai)
    db.commit()
    db.refresh(loai)
    return loai

def get_all_loai_nguoi_dung(db: Session):
    return db.exec(select(LoaiNguoiDung).where(LoaiNguoiDung.deleted_at.is_(None))).all()

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

def soft_delete_loai_nguoi_dung(db: Session, loai_nguoi_dung_id: int) -> bool:
    loai = db.exec(
        select(LoaiNguoiDung).where(
            LoaiNguoiDung.id == loai_nguoi_dung_id,
            LoaiNguoiDung.deleted_at.is_(None)
        )
    ).first()

    if not loai:
        return False

    loai.deleted_at = utils.get_current_time()
    db.add(loai)
    db.commit()
    return True

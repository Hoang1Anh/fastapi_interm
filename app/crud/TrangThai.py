from sqlmodel import Session, select
from app.models.TrangThai import TrangThai
from app.schemas.TrangThai import TrangThaiCreate, TrangThaiUpdate
from app.models import ThongTinNguoiDung

def change_status(db: Session, user_id: int, status_id: int):
    nguoi_dung = db.get(ThongTinNguoiDung, user_id)
    if not nguoi_dung:
        return None

    nguoi_dung.trang_thai_id = status_id
    db.add(nguoi_dung)
    db.commit()
    db.refresh(nguoi_dung)

    return nguoi_dung

def create_trang_thai(db: Session, data: TrangThaiCreate):
    trang_thai = TrangThai(**data.dict())
    db.add(trang_thai)
    db.commit()
    db.refresh(trang_thai)
    return trang_thai

def get_all_trang_thai(db: Session):
    return db.exec(select(TrangThai)).all()

def update_trang_thai(db: Session, trang_thai_id: int, data: TrangThaiUpdate):
    trang_thai = db.get(TrangThai, trang_thai_id)
    if not trang_thai:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(trang_thai, key, value)
    db.add(trang_thai)
    db.commit()
    db.refresh(trang_thai)
    return trang_thai

def delete_trang_thai(db: Session, trang_thai_id: int):
    trang_thai = db.get(TrangThai, trang_thai_id)
    if not trang_thai:
        return None
    db.delete(trang_thai)
    db.commit()
    return True

from sqlmodel import Session, select
from app.models import NhomQuyen
from app.schemas.NhomQuyen import NhomQuyenCreate, NhomQuyenUpdate
from app import utils

def create_nhom_quyen(db: Session, data: NhomQuyenCreate) -> NhomQuyen:
    nhom_quyen = NhomQuyen(**data.dict())
    db.add(nhom_quyen)
    db.commit()
    db.refresh(nhom_quyen)
    return nhom_quyen

def get_all_nhom_quyen(db: Session):
    return db.exec(select(NhomQuyen).where(NhomQuyen.deleted_at.is_(None))).all()

def update_nhom_quyen(db: Session, nhom_quyen_id: int, data: NhomQuyenUpdate):
    nhom_quyen = db.exec(select(NhomQuyen).where(NhomQuyen.id == nhom_quyen_id, NhomQuyen.deleted_at.is_(None))).first()
    if not nhom_quyen:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(nhom_quyen, key, value)
    nhom_quyen.updated_at = utils.get_current_time()
    db.commit()
    db.refresh(nhom_quyen)
    return nhom_quyen

def soft_delete_nhom_quyen(db: Session, nhom_quyen_id: int):
    nhom_quyen = db.exec(select(NhomQuyen).where(NhomQuyen.id == nhom_quyen_id, NhomQuyen.deleted_at.is_(None))).first()
    if not nhom_quyen:
        return None
    nhom_quyen.deleted_at = utils.get_current_time()
    db.commit()
    return nhom_quyen

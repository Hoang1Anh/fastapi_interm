from sqlmodel import Session, select
from app.models.LichSuChamSoc import LichSuChamSoc
from app.schemas.LichSuChamSoc import LichSuChamSocCreate, LichSuChamSocUpdate
from typing import List

def create_lich_su_cham_soc(db: Session, data: LichSuChamSocCreate):
    cham_soc = LichSuChamSoc(**data.dict())
    db.add(cham_soc)
    db.commit()
    db.refresh(cham_soc)
    return cham_soc

def get_lich_su_cham_soc_by_hoc_sinh_id(db: Session, thong_tin_hoc_sinh_id: int) -> List[LichSuChamSoc]:
    result = db.exec(
        select(LichSuChamSoc).where(LichSuChamSoc.thong_tin_hoc_sinh_id == thong_tin_hoc_sinh_id)
    ).all()
    return result

def update_lich_su_cham_soc(db: Session, cham_soc_id: int, data: LichSuChamSocUpdate):
    cham_soc = db.get(LichSuChamSoc, cham_soc_id)
    if not cham_soc:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cham_soc, key, value)
    db.add(cham_soc)
    db.commit()
    db.refresh(cham_soc)
    return cham_soc

def delete_lich_su_cham_soc(db: Session, cham_soc_id: int):
    cham_soc = db.get(LichSuChamSoc, cham_soc_id)
    if not cham_soc:
        return None
    db.delete(cham_soc)
    db.commit()
    return True

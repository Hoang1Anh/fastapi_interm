from sqlmodel import Session, select, delete
from app.models import QuyenCuaNhom
from typing import List

def assign_quyen_cho_nhom(db: Session, nhom_quyen_id: int, quyen_ids: List[int]) -> None:
    db.exec(
        delete(QuyenCuaNhom).where(QuyenCuaNhom.nhom_quyen_id == nhom_quyen_id)
    )

    for quyen_id in quyen_ids:
        quyen_nhom = QuyenCuaNhom(nhom_quyen_id=nhom_quyen_id, quyen_id=quyen_id)
        db.add(quyen_nhom)

    db.commit()

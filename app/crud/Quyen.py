from sqlmodel import Session, select
from app.models import Quyen
from app.schemas.Quyen import QuyenCreate, QuyenUpdate
from app.utils import get_current_time


def create_quyen(db: Session, quyen_data: QuyenCreate) -> Quyen:
    quyen = Quyen(**quyen_data.dict())
    quyen.created_at = get_current_time()
    db.add(quyen)
    db.commit()
    db.refresh(quyen)
    return quyen


def get_all_quyen(db: Session) -> list[Quyen]:
    return db.exec(select(Quyen).where(Quyen.deleted_at.is_(None))).all()


def get_quyen_by_id(db: Session, quyen_id: int) -> Quyen | None:
    return db.exec(
        select(Quyen).where(
            Quyen.id == quyen_id,
            Quyen.deleted_at.is_(None)
        )
    ).first()


def update_quyen(db: Session, quyen_id: int, data: QuyenUpdate) -> Quyen | None:
    quyen = get_quyen_by_id(db, quyen_id)
    if not quyen:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(quyen, key, value)
    quyen.updated_at = get_current_time()
    db.add(quyen)
    db.commit()
    db.refresh(quyen)
    return quyen


def soft_delete_quyen(db: Session, quyen_id: int) -> bool:
    quyen = get_quyen_by_id(db, quyen_id)
    if not quyen:
        return False
    quyen.deleted_at = get_current_time()
    db.add(quyen)
    db.commit()
    return True

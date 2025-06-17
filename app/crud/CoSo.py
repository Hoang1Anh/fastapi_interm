from sqlmodel import Session, select
from app.models.CoSo import CoSo
from app.schemas.CoSo import CoSoCreate, CoSoUpdate
from app import utils
def create_co_so(db: Session, data: CoSoCreate):
    co_so = CoSo(**data.dict())
    db.add(co_so)
    db.commit()
    db.refresh(co_so)
    return co_so

def get_all_co_so(db: Session):
    return db.exec(select(CoSo).where(CoSo.deleted_at.is_(None))).all()

def update_co_so(db: Session, co_so_id: int, data: CoSoUpdate):
    co_so = db.get(CoSo, co_so_id)
    if not co_so:
        return None
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(co_so, key, value)
    db.add(co_so)
    db.commit()
    db.refresh(co_so)
    return co_so

def delete_co_so(db: Session, co_so_id: int) -> bool:
    co_so = db.exec(
        select(CoSo).where(
            CoSo.id == co_so_id,
            CoSo.deleted_at.is_(None)
        )
    ).first()

    if not co_so:
        return False

    co_so.deleted_at = utils.get_current_time()
    db.add(co_so)
    db.commit()
    return True

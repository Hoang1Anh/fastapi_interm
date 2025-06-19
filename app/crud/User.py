from typing import Optional, List
from sqlmodel import Session, select
from app.models import User, ThongTinNguoiDung
from app.schemas.User import UserCreate, UserUpdate
from app import utils
from app.auth import hash_password

def create_user(db: Session, data: UserCreate) -> User:
    # 1. Tạo ThongTinNguoiDung
    thong_tin_data = data.thong_tin_nguoi_dung
    thong_tin = ThongTinNguoiDung(**thong_tin_data.dict())
    db.add(thong_tin)
    db.commit()
    db.refresh(thong_tin)

    # 2. Tạo User có liên kết Thong_tin_id
    user = User(
        ten_dang_nhap=data.ten_dang_nhap,
        password=hash_password(data.password),
        nhom_quyen_id=data.nhom_quyen_id,
        thong_tin_id=thong_tin.id,
        is_admin=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "Thêm thành công", "user_id": user.id} 

def get_all_users(db: Session) -> List[User]:
    return db.exec(
        select(User).where(User.deleted_at.is_(None))
    ).all()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    user = db.get(User, user_id)
    if not user or user.deleted_at is not None:
        return None
    return user


def update_user(db: Session, user_id: int, data: UserUpdate) -> Optional[User]:
    user = db.get(User, user_id)
    if not user or user.deleted_at is not None:
        return None

    update_data = data.dict(exclude_unset=True)
    update_data.pop("is_admin", None)

    for key, value in update_data.items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def soft_delete_user(db: Session, user_id: int) -> Optional[dict]:
    user = db.get(User, user_id)
    if not user or user.deleted_at is not None:
        return None

    user.deleted_at = utils.get_current_time()

    db.add(user)
    db.commit()
    return {"message": "Xoá mềm thành công"}

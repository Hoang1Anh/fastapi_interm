from typing import Optional, List
from sqlmodel import Session, select
from app.models import User
from app.schemas.User import UserCreate, UserUpdate
from app import utils


def create_user(db: Session, data: UserCreate) -> User:
    user = User(**data.dict(), is_admin=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


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

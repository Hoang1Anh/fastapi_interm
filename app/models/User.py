from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from datetime import datetime
from .ModelChung import ModelChung
from uuid import uuid4

class User(ModelChung, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(default_factory=lambda: str(uuid4()), index=True, nullable=False)
    ten_dang_nhap: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
    email_verified_at: Optional[datetime] = None
    remember_token: Optional[str] = None
    is_admin: bool = Field(default=False, nullable=False)

    # Foreign Keys
    thong_tin_id: int = Field(foreign_key="thong_tin_nguoi_dung.id", nullable=False)
    nhom_quyen_id: int = Field(foreign_key="nhom_quyen.id", nullable=False)

    # Relationships
    nhom_quyen: Optional["NhomQuyen"] = Relationship(back_populates="users")
    thong_tin_nguoi_dung: Optional["ThongTinNguoiDung"] = Relationship(back_populates="user")

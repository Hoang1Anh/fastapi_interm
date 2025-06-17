from sqlmodel import Field, Relationship
from typing import Optional
from datetime import datetime
from .ModelChung import ModelChung

class User(ModelChung, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    ten_dang_nhap: str
    email_verified_at: Optional[datetime] = None
    password: str
    remember_token: Optional[str] = None
    is_admin: Optional[bool] = Field(default=False)

    # Foreign Keys
    thong_tin_id: int = Field(foreign_key="thong_tin_nguoi_dung.id")
    nhom_quyen_id: int = Field(foreign_key="nhom_quyen.id")

    # Relationships
    nhom_quyen: Optional["NhomQuyen"] = Relationship(back_populates="users")
    thong_tin_nguoi_dung: Optional["ThongTinNguoiDung"] = Relationship(back_populates="user")
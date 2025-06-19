from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.ThongTinNguoiDung import ThongTinNguoiDungCreate, ThongTinNguoiDungRead


class UserBase(SQLModel):
    ten_dang_nhap: str
    nhom_quyen_id: int
    email_verified_at: Optional[datetime] = None
    remember_token: Optional[str] = None

class UserCreate(UserBase):
    password: str
    thong_tin_nguoi_dung: ThongTinNguoiDungCreate

class UserRead(UserBase):
    id: int
    uuid: str
    is_admin: bool
    thong_tin_id: int
    thong_tin_nguoi_dung: Optional[ThongTinNguoiDungRead] = None

class UserUpdate(SQLModel):
    ten_dang_nhap: Optional[str] = None
    password: Optional[str] = None
    nhom_quyen_id: Optional[int] = None
    email_verified_at: Optional[datetime] = None
    remember_token: Optional[str] = None

class UserLogin(SQLModel):
    ten_dang_nhap: str
    password: str

class Token(SQLModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"

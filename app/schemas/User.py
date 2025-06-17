from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class UserBase(SQLModel):
    ten_dang_nhap: str
    password: str
    thong_tin_id: int
    nhom_quyen_id: int
    email_verified_at: Optional[datetime] = None
    remember_token: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    uuid: str
    is_admin: bool

class UserUpdate(SQLModel):
    ten_dang_nhap: Optional[str] = None
    password: Optional[str] = None
    thong_tin_id: Optional[int] = None
    nhom_quyen_id: Optional[int] = None
    email_verified_at: Optional[datetime] = None
    remember_token: Optional[str] = None

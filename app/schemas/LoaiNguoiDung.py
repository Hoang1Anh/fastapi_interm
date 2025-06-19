from sqlmodel import SQLModel, Field
from typing import Optional
import uuid as uuid_lib

class LoaiNguoiDungBase(SQLModel):
    ten_loai_nguoi_dung: str = Field(max_length=50)
    nhom_nguoi_dung: Optional[str] = Field(default=None, max_length=255)

class LoaiNguoiDungCreate(LoaiNguoiDungBase):
    pass

class LoaiNguoiDungRead(LoaiNguoiDungBase):
    id: int
    uuid: str

class LoaiNguoiDungUpdate(SQLModel):
    ten_loai_nguoi_dung: Optional[str] = None
    nhom_nguoi_dung: Optional[str] = None

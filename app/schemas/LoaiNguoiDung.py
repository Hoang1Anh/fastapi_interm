from sqlmodel import Field
from typing import Optional
import uuid as uuid_lib
from .SchemaChung import SchemaChung

class LoaiNguoiDungBase(SchemaChung):
    ten_loai_nguoi_dung: str = Field(max_length=50)
    nhom_nguoi_dung: Optional[str] = Field(default=None, max_length=255)

class LoaiNguoiDungCreate(LoaiNguoiDungBase):
    uuid: str = Field(default_factory=lambda: str(uuid_lib.uuid4()))

class LoaiNguoiDungRead(LoaiNguoiDungBase):
    id: int
    uuid: str

class LoaiNguoiDungUpdate(SchemaChung):
    ten_loai_nguoi_dung: Optional[str] = None
    nhom_nguoi_dung: Optional[str] = None

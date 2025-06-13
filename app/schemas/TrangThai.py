from sqlmodel import Field
from typing import Optional
import uuid as uuid_lib
from .SchemaChung import SchemaChung

class TrangThaiBase(SchemaChung):
    ma_trang_thai: str = Field(max_length=50)
    ten_trang_thai: str = Field(max_length=50)
    nhom_trang_thai: Optional[str] = None

class TrangThaiCreate(TrangThaiBase):
    pass

class TrangThaiRead(TrangThaiBase):
    id: int

class TrangThaiUpdate(SchemaChung):
    ma_trang_thai: Optional[str] = None
    ten_trang_thai: Optional[str] = None
    nhom_trang_thai: Optional[str] = None

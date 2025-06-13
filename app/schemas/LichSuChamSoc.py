from sqlmodel import Field
from typing import Optional
from datetime import datetime
import uuid as uuid_lib
from .SchemaChung import SchemaChung

class LichSuChamSocBase(SchemaChung):
    noi_dung: Optional[str] = None
    thoi_gian: Optional[datetime] = None
    nhan_vien_id: int
    thong_tin_hoc_sinh_id: Optional[int] = None

class LichSuChamSocCreate(LichSuChamSocBase):
    pass

class LichSuChamSocRead(LichSuChamSocBase):
    id: int

class LichSuChamSocUpdate(SchemaChung):
    noi_dung: Optional[str] = None
    thoi_gian: Optional[datetime] = None
    nhan_vien_id: Optional[int] = None
    thong_tin_hoc_sinh_id: Optional[int] = None

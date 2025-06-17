from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid as uuid_lib

class LichSuChamSocBase(SQLModel):
    noi_dung: Optional[str] = None
    thoi_gian: Optional[datetime] = None
    nhan_vien_id: int
    thong_tin_hoc_sinh_id: Optional[int] = None

class LichSuChamSocCreate(LichSuChamSocBase):
    pass

class LichSuChamSocRead(LichSuChamSocBase):
    id: int

class LichSuChamSocUpdate(SQLModel):
    noi_dung: Optional[str] = None
    thoi_gian: Optional[datetime] = None
    nhan_vien_id: Optional[int] = None
    thong_tin_hoc_sinh_id: Optional[int] = None

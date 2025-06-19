from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class ThongTinNguoiDungBase(SQLModel):
    ho_ten: str
    gioi_tinh: Optional[str] = None
    ngay_sinh: Optional[datetime] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    email: Optional[str] = None
    loai_nguoi_dung_id: Optional[int] = None
    co_so_id: Optional[int] = None
    trang_thai_id: Optional[int] = None
    ip_address: Optional[str] = None

class ThongTinNguoiDungCreate(ThongTinNguoiDungBase):
    pass
class ThongTinNguoiDungRead(ThongTinNguoiDungBase):
    id: int

class ThongTinNguoiDungUpdate(SQLModel):
    ho_ten: Optional[str] = None
    gioi_tinh: Optional[str] = None
    ngay_sinh: Optional[datetime] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    email: Optional[str] = None
    loai_nguoi_dung_id: Optional[int] = None
    co_so_id: Optional[int] = None
    trang_thai_id: Optional[int] = None
    ip_address: Optional[str] = None

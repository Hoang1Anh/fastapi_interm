from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime
from app.schemas.ThongTinNguoiDung import ThongTinNguoiDungCreate

# Schemas cho ThongTinHocSinh

class ThongTinHocSinhBase(SQLModel):
    lop: Optional[str] = None
    truong: Optional[str] = None
    ho_ten_ph: Optional[str] = None
    sdt_ph: Optional[str] = None
    email_ph: Optional[str] = None
    nguoi_gioi_thieu: Optional[str] = None
    ghi_chu: Optional[str] = None
    import_date: Optional[datetime] = None

class ThongTinHocSinhCreate(ThongTinHocSinhBase):
    pass

class ThongTinHocSinhRead(ThongTinHocSinhBase):
    id: int
    thong_tin_id: int

class ThongTinHocSinhUpdate(SQLModel):
    lop: Optional[str] = None
    truong: Optional[str] = None
    ho_ten_ph: Optional[str] = None
    sdt_ph: Optional[str] = None
    email_ph: Optional[str] = None
    nguoi_gioi_thieu: Optional[str] = None
    ghi_chu: Optional[str] = None
    import_date: Optional[datetime] = None

# Schema tổng hợp để insert

class InsertHocSinh(SQLModel):
    nguoi_dung: ThongTinNguoiDungCreate
    hoc_sinh: ThongTinHocSinhCreate

# Schema để lọc
class HocSinhFilter(SQLModel):
    keyword: Optional[str] = None
    cham_soc_tu_ngay: Optional[datetime] = None
    cham_soc_den_ngay: Optional[datetime] = None
    nam_sinh: Optional[int] = None
    nhan_vien_id: Optional[int] = None
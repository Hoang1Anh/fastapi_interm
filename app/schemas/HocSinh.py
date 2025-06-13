from sqlmodel import Field
from typing import Optional
from datetime import datetime
import uuid as uuid_lib
from .SchemaChung import SchemaChung
# Schemas cho ThongTinNguoiDung

class ThongTinNguoiDungBase(SchemaChung):
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
    uuid: str = Field(default_factory=lambda: str(uuid_lib.uuid4()))

class ThongTinNguoiDungRead(ThongTinNguoiDungBase):
    id: int
    uuid: str

class ThongTinNguoiDungUpdate(SchemaChung):
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

# Schemas cho ThongTinHocSinh

class ThongTinHocSinhBase(SchemaChung):
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

class ThongTinHocSinhUpdate(SchemaChung):
    lop: Optional[str] = None
    truong: Optional[str] = None
    ho_ten_ph: Optional[str] = None
    sdt_ph: Optional[str] = None
    email_ph: Optional[str] = None
    nguoi_gioi_thieu: Optional[str] = None
    ghi_chu: Optional[str] = None
    import_date: Optional[datetime] = None

# Schema tổng hợp để insert

class InsertHocSinh(SchemaChung):
    nguoi_dung: ThongTinNguoiDungCreate
    hoc_sinh: ThongTinHocSinhCreate

# Schema để lọc
class HocSinhFilter(SchemaChung):
    keyword: Optional[str] = None
    cham_soc_tu_ngay: Optional[datetime] = None
    cham_soc_den_ngay: Optional[datetime] = None
    nam_sinh: Optional[int] = None
    nhan_vien_id: Optional[int] = None
from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional, List
from .ModelChung import ModelChung


class ThongTinNguoiDung(ModelChung, table=True):
    """
    Model for user information.
    """
    __tablename__ = 'thong_tin_nguoi_dung'

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(unique=True, index=True)
    ho_ten: str = Field(max_length=255)
    gioi_tinh: Optional[str] = Field(default=None, max_length=10)
    ngay_sinh: Optional[datetime] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = Field(default=None, max_length=15)
    email: Optional[str] = Field(default=None, max_length=255)

    # Foreign Keys
    loai_nguoi_dung_id: Optional[int] = Field(default=None, foreign_key="loai_nguoi_dung.id")
    co_so_id: Optional[int] = Field(default=None, foreign_key="co_so.id")
    trang_thai_id: Optional[int] = Field(default=None, foreign_key="trang_thai.id")
    
    ip_address: Optional[str] = Field(default=None, max_length=45)
    
    # Relationships
    thong_tin_hoc_sinh: List["ThongTinHocSinh"] = Relationship(back_populates="thong_tin_nguoi_dung")
    lich_su_cham_soc: List["LichSuChamSoc"] = Relationship(back_populates="thong_tin_nguoi_dung")
    co_so: Optional["CoSo"] = Relationship(back_populates="thong_tin_nguoi_dung")
    loai_nguoi_dung: Optional["LoaiNguoiDung"] = Relationship(back_populates="thong_tin_nguoi_dung")
    trang_thai: Optional["TrangThai"] = Relationship(back_populates="thong_tin_nguoi_dung")
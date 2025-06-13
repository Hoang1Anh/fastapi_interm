from sqlmodel import Field, Relationship
from typing import Optional, List
from .ModelChung import ModelChung

class TrangThai(ModelChung, table=True):
    """
        Model for status.
    """
    __tablename__ = 'trang_thai'

    id: Optional[int] = Field(default=None, primary_key=True)
    ma_trang_thai: str = Field(unique=True, index=True, max_length=50)
    ten_trang_thai: str = Field(max_length=50, index=True)
    nhom_trang_thai: Optional[str] = Field(default=None, max_length=255)

    # Relationships
    thong_tin_nguoi_dung: List["ThongTinNguoiDung"] = Relationship(back_populates="trang_thai")
    co_so: List["CoSo"] = Relationship(back_populates="trang_thai")
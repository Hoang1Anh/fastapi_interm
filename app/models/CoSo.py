from sqlmodel import Field, Relationship
from typing import Optional , List
from .ModelChung import ModelChung

class CoSo(ModelChung, table=True):
    """
        Model for educational institution information.
    """
    __tablename__ = 'co_so'

    id: Optional[int] = Field(default=None, primary_key=True)
    ten_co_so: str = Field(max_length=255, index=True)
    dia_chi_co_so: Optional[str] = Field(default=None, max_length=255)
    sdt: Optional[str] = Field(default=None, max_length=15)
    email: Optional[str] = Field(default=None, max_length=255)
    
    # Foreign Keys
    trang_thai_id: Optional[int] = Field(default=None, foreign_key="trang_thai.id")

    # Relationships
    thong_tin_nguoi_dung: List["ThongTinNguoiDung"] = Relationship(back_populates="co_so")
    trang_thai: Optional["TrangThai"] = Relationship(back_populates="co_so")
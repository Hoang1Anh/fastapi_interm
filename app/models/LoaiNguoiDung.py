from sqlmodel import Field, Relationship
from typing import Optional , List
from .ModelChung import ModelChung

class LoaiNguoiDung(ModelChung, table=True):
    """
        Model for user type.
    """
    __tablename__ = 'loai_nguoi_dung'

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(unique=True, index=True)
    ten_loai_nguoi_dung: str = Field(max_length=50, index=True)
    nhom_nguoi_dung: Optional[str] = Field(default=None, max_length=255)

    # Relationships
    thong_tin_nguoi_dung: List["ThongTinNguoiDung"] = Relationship(back_populates="loai_nguoi_dung")
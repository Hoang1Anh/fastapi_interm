from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional, List
from .ModelChung import ModelChung


class ThongTinHocSinh(ModelChung, table=True):
    """
        Model for student information.
    """
    __tablename__ = 'thong_tin_hoc_sinh'

    id: Optional[int] = Field(default=None, primary_key=True)
    lop: Optional[str] = Field(default=None, max_length=50)
    truong: Optional[str] = Field(default=None, max_length=255)
    ho_ten_ph: Optional[str] = Field(default=None, max_length=255)
    sdt_ph: Optional[str] = Field(default=None, max_length=15)
    email_ph: Optional[str] = Field(default=None, max_length=255)
    nguoi_gioi_thieu: Optional[str] = Field(default=None, max_length=255)
    ghi_chu: Optional[str] = None
    import_date: Optional[datetime] = Field(default=None)

    # Foreign Keys
    thong_tin_id: Optional[int] = Field(foreign_key="thong_tin_nguoi_dung.id")

    # Relationships
    thong_tin_nguoi_dung: Optional["ThongTinNguoiDung"] = Relationship(back_populates="thong_tin_hoc_sinh")
    lich_su_cham_soc: List["LichSuChamSoc"] = Relationship(back_populates="thong_tin_hoc_sinh")

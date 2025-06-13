from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional , List
from .ModelChung import ModelChung

class LichSuChamSoc(ModelChung, table=True):
    """
        Model for care history.
    """
    
    __tablename__ = 'lich_su_cham_soc'

    id: Optional[int] = Field(default=None, primary_key=True)
    noi_dung: Optional[str] = None
    thoi_gian: Optional[datetime] = None

    # Foreign Keys
    nhan_vien_id: int = Field(foreign_key="thong_tin_nguoi_dung.id")
    thong_tin_hoc_sinh_id: Optional[int] = Field(default=None, foreign_key="thong_tin_hoc_sinh.id")

    # Relationships
    thong_tin_nguoi_dung: List["ThongTinNguoiDung"] = Relationship(back_populates="lich_su_cham_soc")
    thong_tin_hoc_sinh: List["ThongTinHocSinh"] = Relationship(back_populates="lich_su_cham_soc")


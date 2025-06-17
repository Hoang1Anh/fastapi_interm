from sqlmodel import Field
from typing import Optional
from .ModelChung import ModelChung

class LichSuHeThong(ModelChung, table=True):
    __tablename__ = "lich_su_he_thong"

    id: Optional[int] = Field(default=None, primary_key=True)
    noi_dung: Optional[str] = Field(default=None, max_length=255)
    url: Optional[str] = Field(default=None, max_length=255)
    du_lieu_vao: Optional[str] = Field(default=None, max_length=1000)
    du_lieu_ra: Optional[str] = Field(default=None, max_length=1000)
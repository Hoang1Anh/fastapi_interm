from uuid import uuid4
from sqlmodel import SQLModel, Field
from typing import Optional

class NhomQuyenBase(SQLModel):
    ma_nhom_quyen: str
    ten_nhom_quyen: str
    mo_ta: Optional[str] = None

class NhomQuyenCreate(NhomQuyenBase):
    pass
class NhomQuyenUpdate(SQLModel):
    ma_nhom_quyen: Optional[str] = None
    ten_nhom_quyen: Optional[str] = None
    mo_ta: Optional[str] = None

class NhomQuyenRead(NhomQuyenBase):
    id: int
    uuid: str

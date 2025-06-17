from uuid import uuid4
from sqlmodel import SQLModel, Field
from typing import Optional

class QuyenBase(SQLModel):
    ma: str
    ten: str
    mo_ta: Optional[str] = None

class QuyenCreate(QuyenBase):
    pass

class QuyenUpdate(SQLModel):
    ma: Optional[str] = None
    ten: Optional[str] = None
    mo_ta: Optional[str] = None

class QuyenRead(QuyenBase):
    id: int
    uuid: str

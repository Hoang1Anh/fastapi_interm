from sqlmodel import Field, Relationship
from typing import Optional, List
from .ModelChung import ModelChung
from uuid import uuid4

class Quyen(ModelChung, table=True):
    __tablename__ = "quyen"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(default_factory=lambda: str(uuid4()), nullable=False, index=True)
    ma: str = Field(nullable=False, index=True)
    ten: str = Field(nullable=False)
    mo_ta: Optional[str] = Field(default=None)

    # Relationship
    quyen_cua_nhom: List["QuyenCuaNhom"] = Relationship(back_populates="quyen")

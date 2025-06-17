from sqlmodel import Field, Relationship
from typing import Optional
from .ModelChung import ModelChung

class QuyenCuaNhom(ModelChung, table=True):
    __tablename__ = "quyen_cua_nhom"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Foreign Keys
    quyen_id: int = Field(foreign_key="quyen.id")
    nhom_quyen_id: int = Field(foreign_key="nhom_quyen.id")

    # Relationships
    quyen: Optional["Quyen"] = Relationship(back_populates="quyen_cua_nhom")
    nhom_quyen: Optional["NhomQuyen"] = Relationship(back_populates="quyen_cua_nhom")

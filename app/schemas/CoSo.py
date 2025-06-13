from sqlmodel import Field
from typing import Optional
import uuid as uuid_lib
from .SchemaChung import SchemaChung

class CoSoBase(SchemaChung):
    ten_co_so: str = Field(max_length=255)
    dia_chi_co_so: Optional[str] = None
    sdt: Optional[str] = None
    email: Optional[str] = None
    trang_thai_id: Optional[int] = None

class CoSoCreate(CoSoBase):
    pass
class CoSoRead(CoSoBase):
    id: int

class CoSoUpdate(SchemaChung):
    ten_co_so: Optional[str] = None
    dia_chi_co_so: Optional[str] = None
    sdt: Optional[str] = None
    email: Optional[str] = None
    trang_thai_id: Optional[int] = None

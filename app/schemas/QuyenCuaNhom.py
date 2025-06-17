from sqlmodel import SQLModel
from typing import List

class QuyenAssignRequest(SQLModel):
    nhom_quyen_id: int
    quyen_ids: List[int]
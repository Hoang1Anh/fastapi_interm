from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class SchemaChung(SQLModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None
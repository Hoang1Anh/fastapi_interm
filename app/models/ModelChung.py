from sqlmodel import SQLModel, Field
from ..utils import get_current_time
from typing import Optional

class ModelChung(SQLModel):
    """
        Base model for all database models.
    """
    __abstract__ = True

    created_at: Optional[str] = Field(default_factory=get_current_time)
    updated_at: Optional[str] = Field(default_factory=get_current_time)
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None
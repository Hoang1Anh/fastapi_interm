from pydantic import BaseModel
from datetime import datetime

class FileSchema(BaseModel):
    id: int
    filename: str
    hash: str
    content_type: str
    upload_time: datetime

    class Config:
        orm_mode = True
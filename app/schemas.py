from pydantic import BaseModel
from datetime import datetime

class FileOut(BaseModel):
    id: int
    filename: str
    content_type: str
    size: int
    upload_time: datetime
    # path: str

    class Config:
        orm_mode = True
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class AudioFile(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    hash = Column(String(64), unique=True)
    upload_time = Column(DateTime, default=datetime.utcnow)
    content_type = Column(String(100))
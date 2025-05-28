from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    hash = Column(String(64), unique=True, nullable=False)
    content_type = Column(String(100))
    size = Column(Integer)
    upload_time = Column(DateTime, default=datetime.utcnow)
    # path = Column(String(255))




    #khi xóa đi 1 trường trong model thì code ko update được lên database nên trường đã xóa trên databse vẫn còn dẫn đến khi chyaj báo lôi
    #khi thêm 1 trường bất kì cũng tương tự do databse ko nhận được code nên trường trong databse ko có
    #dùng migration
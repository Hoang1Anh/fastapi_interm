import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from app.models import *

# Load biến môi trường từ file .env
load_dotenv()

# Lấy thông tin kết nối từ .env
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", os.getenv("MYSQL_ROOT_PASSWORD"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

# Chuỗi kết nối SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# Tạo engine kết nối MySQL
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """
    Create database and table if not exist.
    """
    SQLModel.metadata.create_all(engine)
    

# Dependency cho FastAPI để lấy session kết nối database
def get_session():
    with Session(engine) as session:
        yield session
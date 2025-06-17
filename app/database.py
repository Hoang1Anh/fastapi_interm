import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session
from fastapi import Request
from app.models.ModelChung import ModelChung
from app import utils

# Load biến môi trường từ file .env
load_dotenv()

# Lấy thông tin kết nối từ biến môi trường
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", os.getenv("MYSQL_ROOT_PASSWORD", ""))
MYSQL_DB = os.getenv("MYSQL_DB", "mydatabase")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

# Tạo chuỗi kết nối MySQL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# Tạo engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=5,
    max_overflow=10,
    connect_args={"charset": "utf8mb4"},
)

# Session factory
SessionLocal = sessionmaker(
    class_=Session,
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Tạo bảng nếu chưa có
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency lấy session và inject request
def get_db(request: Request):
    db = SessionLocal()
    db.info["request"] = request  # Gắn request vào session
    try:
        yield db
    finally:
        db.close()

# Hàm gắn các metadata chung
def apply_common_fields(obj, request: Request, is_create: bool = False):
    now = utils.get_current_time()
    user_id = request.state.user_id
    ip_address = request.state.ip_address

    obj.updated_at = now
    obj.updated_by_user_id = user_id
    obj.ip_address = ip_address

    if is_create:
        obj.created_at = now
        obj.created_by_user_id = user_id

@event.listens_for(SessionLocal, "before_flush")
def auto_set_metadata(session, flush_context, instances):
    request = session.info.get("request")
    if not request:
        return

    for obj in session.new:
        if isinstance(obj, ModelChung):
            apply_common_fields(obj, request, is_create=True)

    for obj in session.dirty:
        if isinstance(obj, ModelChung):
            apply_common_fields(obj, request, is_create=False)
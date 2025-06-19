from fastapi import FastAPI
from app.middleware.LichSuHeThong import LichSuHeThongMiddleware
from app.middleware.TruongChung import TruongChungMiddleware
from app.database import create_db_and_tables
from app.routers import (
    HocSinh,
    LoaiNguoiDung,
    CoSo,
    TrangThai,
    LichSuChamSoc,
    NhomQuyen,
    Quyen,
    User,
    Auth,

)

app = FastAPI()

# Đăng ký middleware
app.add_middleware(LichSuHeThongMiddleware)
app.add_middleware(TruongChungMiddleware)

# Tạo bảng khi khởi động
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Gắn router với prefix /api và tags tương ứng
app.include_router(HocSinh.router, prefix="/api", tags=["HocSinh"])
app.include_router(LoaiNguoiDung.router, prefix="/api", tags=["LoaiNguoiDung"])
app.include_router(CoSo.router, prefix="/api", tags=["CoSo"])
app.include_router(TrangThai.router, prefix="/api", tags=["TrangThai"])
app.include_router(LichSuChamSoc.router, prefix="/api", tags=["LichSuChamSoc"])
app.include_router(NhomQuyen.router, prefix="/api", tags=["NhomQuyen"])
app.include_router(Quyen.router, prefix="/api", tags=["Quyen"])
app.include_router(User.router, prefix="/api", tags=["User"])
app.include_router(Auth.router, prefix="/api", tags=["Auth"])




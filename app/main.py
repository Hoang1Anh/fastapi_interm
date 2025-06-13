from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import (
    HocSinh,
    LoaiNguoiDung,
    CoSo,
    TrangThai,
    LichSuChamSoc
)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include tất cả các routers
app.include_router(HocSinh.router, prefix="/api", tags=["HocSinh"])
app.include_router(LoaiNguoiDung.router, prefix="/api", tags=["LoaiNguoiDung"])
app.include_router(CoSo.router, prefix="/api", tags=["CoSo"])
app.include_router(TrangThai.router, prefix="/api", tags=["TrangThai"])
app.include_router(LichSuChamSoc.router, prefix="/api", tags=["LichSuChamSoc"])

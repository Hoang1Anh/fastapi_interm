from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from app.schemas.LoaiNguoiDung import LoaiNguoiDungCreate, LoaiNguoiDungRead, LoaiNguoiDungUpdate
from app.crud import LoaiNguoiDung as crud
from app.database import get_db

router = APIRouter(
    prefix="/loai_nguoi_dung",
    tags=["LoaiNguoiDung"]
)

@router.post("/", response_model=LoaiNguoiDungRead)
def create_loai_nguoi_dung(data: LoaiNguoiDungCreate, db: Session = Depends(get_db)):
    try:
        created = crud.create_loai_nguoi_dung(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo loại người dùng thành công", "data": created.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo loại người dùng: {str(e)}")


@router.get("/", response_model=list[LoaiNguoiDungRead])
def get_all_loai_nguoi_dung(db: Session = Depends(get_db)):
    try:
        result = crud.get_all_loai_nguoi_dung(db)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy loại người dùng nào")
        return JSONResponse(status_code=200, content={"message": "Lấy danh sách loại người dùng thành công", "data": [r.dict() for r in result]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách: {str(e)}")


@router.put("/{loai_nguoi_dung_id}", response_model=LoaiNguoiDungRead)
def update_loai_nguoi_dung(loai_nguoi_dung_id: int, data: LoaiNguoiDungUpdate, db: Session = Depends(get_db)):
    try:
        result = crud.update_loai_nguoi_dung(db, loai_nguoi_dung_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Loại người dùng không tồn tại")
        return JSONResponse(status_code=200, content={"message": "Cập nhật loại người dùng thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật: {str(e)}")


@router.delete("/{loai_nguoi_dung_id}")
def delete_loai_nguoi_dung(loai_nguoi_dung_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.soft_delete_loai_nguoi_dung(db, loai_nguoi_dung_id)
        if not result:
            raise HTTPException(status_code=404, detail="Loại người dùng không tồn tại hoặc đã bị xoá")
        return JSONResponse(status_code=200, content={"message": "Đã xoá loại người dùng thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá: {str(e)}")

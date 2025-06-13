from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.LoaiNguoiDung import LoaiNguoiDungCreate, LoaiNguoiDungRead, LoaiNguoiDungUpdate
from app.crud import LoaiNguoiDung as crud
from app.database import get_session

router = APIRouter(
    prefix="/loai_nguoi_dung",
    tags=["LoaiNguoiDung"]
)

@router.post("/", response_model=LoaiNguoiDungRead)
def create_loai_nguoi_dung(data: LoaiNguoiDungCreate, db: Session = Depends(get_session)):
    return crud.create_loai_nguoi_dung(db, data)

@router.get("/", response_model=list[LoaiNguoiDungRead])
def get_all_loai_nguoi_dung(db: Session = Depends(get_session)):
    return crud.get_all_loai_nguoi_dung(db)

@router.put("/{loai_nguoi_dung_id}", response_model=LoaiNguoiDungRead)
def update_loai_nguoi_dung(loai_nguoi_dung_id: int, data: LoaiNguoiDungUpdate, db: Session = Depends(get_session)):
    result = crud.update_loai_nguoi_dung(db, loai_nguoi_dung_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Loại người dùng không tồn tại")
    return result

@router.delete("/{loai_nguoi_dung_id}")
def delete_loai_nguoi_dung(loai_nguoi_dung_id: int, db: Session = Depends(get_session)):
    result = crud.delete_loai_nguoi_dung(db, loai_nguoi_dung_id)
    if not result:
        raise HTTPException(status_code=404, detail="Loại người dùng không tồn tại")
    return {"message": "Xoá thành công"}

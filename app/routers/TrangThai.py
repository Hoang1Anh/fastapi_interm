from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.TrangThai import TrangThaiCreate, TrangThaiRead, TrangThaiUpdate
from app.crud import TrangThai as crud
from app.database import get_session

router = APIRouter(
    prefix="/trang_thai",
    tags=["TrangThai"]
)

@router.post("/", response_model=TrangThaiRead)
def create_trang_thai(data: TrangThaiCreate, db: Session = Depends(get_session)):
    return crud.create_trang_thai(db, data)

@router.get("/", response_model=list[TrangThaiRead])
def get_all_trang_thai(db: Session = Depends(get_session)):
    return crud.get_all_trang_thai(db)

@router.put("/{trang_thai_id}", response_model=TrangThaiRead)
def update_trang_thai(trang_thai_id: int, data: TrangThaiUpdate, db: Session = Depends(get_session)):
    result = crud.update_trang_thai(db, trang_thai_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Trạng thái không tồn tại")
    return result

@router.delete("/{trang_thai_id}")
def delete_trang_thai(trang_thai_id: int, db: Session = Depends(get_session)):
    result = crud.delete_trang_thai(db, trang_thai_id)
    if not result:
        raise HTTPException(status_code=404, detail="Trạng thái không tồn tại")
    return {"message": "Xoá thành công"}

@router.patch("/change_status/{user_id}")
def change_status(user_id: int, status_id: int, db: Session = Depends(get_session)):
    user = crud.change_status(db, user_id, status_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
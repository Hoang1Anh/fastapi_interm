from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.schemas.HocSinh import InsertHocSinh, HocSinhFilter
from app.crud import HocSinh as hoc_sinh_crud

router = APIRouter(prefix="/hoc_sinh", tags=["HocSinh"])

@router.post("/", response_model=dict)
def create_hoc_sinh(data: InsertHocSinh, db: Session = Depends(get_session)):
    return hoc_sinh_crud.create_hoc_sinh(db, data)

@router.post("/filter")
def filter_hoc_sinh(filter: HocSinhFilter, db: Session = Depends(get_session)):
    result = hoc_sinh_crud.get_all_hoc_sinh(db, filter)
    return result

@router.put("/{user_id}", response_model=dict)
def update_hoc_sinh(user_id: int, data: InsertHocSinh, db: Session = Depends(get_session)):
    result = hoc_sinh_crud.update_hoc_sinh(db, user_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy học sinh")
    return result

@router.delete("/{user_id}", response_model=dict)
def delete_hoc_sinh(user_id: int, db: Session = Depends(get_session)):
    result = hoc_sinh_crud.delete_hoc_sinh(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy học sinh")
    return result

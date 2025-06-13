from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.LichSuChamSoc import LichSuChamSocCreate, LichSuChamSocRead, LichSuChamSocUpdate
from app.crud import LichSuChamSoc as crud
from app.database import get_session
from typing import List

router = APIRouter(
    prefix="/lich_su_cham_soc",
    tags=["LichSuChamSoc"]
)

@router.post("/", response_model=LichSuChamSocRead)
def create_lich_su_cham_soc(data: LichSuChamSocCreate, db: Session = Depends(get_session)):
    return crud.create_lich_su_cham_soc(db, data)

@router.get("/hoc_sinh/{thong_tin_hoc_sinh_id}", response_model=List[LichSuChamSocRead])
def get_lich_su_cham_soc_by_hoc_sinh_id(thong_tin_hoc_sinh_id: int, db: Session = Depends(get_session)):
    result = crud.get_lich_su_cham_soc_by_hoc_sinh_id(db, thong_tin_hoc_sinh_id)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc cho học sinh này")
    return result


@router.put("/{cham_soc_id}", response_model=LichSuChamSocRead)
def update_lich_su_cham_soc(cham_soc_id: int, data: LichSuChamSocUpdate, db: Session = Depends(get_session)):
    result = crud.update_lich_su_cham_soc(db, cham_soc_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc")
    return result

@router.delete("/{cham_soc_id}")
def delete_lich_su_cham_soc(cham_soc_id: int, db: Session = Depends(get_session)):
    result = crud.delete_lich_su_cham_soc(db, cham_soc_id)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc")
    return {"message": "Xoá thành công"}

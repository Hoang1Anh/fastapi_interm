from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import List

from app.database import get_db
from app.schemas.LichSuChamSoc import LichSuChamSocCreate, LichSuChamSocRead, LichSuChamSocUpdate
from app.crud import LichSuChamSoc as crud

router = APIRouter(
    prefix="/lich_su_cham_soc",
    tags=["LichSuChamSoc"]
)

@router.post("/", response_model=LichSuChamSocRead)
def create_lich_su_cham_soc(data: LichSuChamSocCreate, db: Session = Depends(get_db)):
    try:
        result = crud.create_lich_su_cham_soc(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo lịch sử chăm sóc thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo lịch sử: {str(e)}")


@router.get("/hoc_sinh/{thong_tin_hoc_sinh_id}", response_model=List[LichSuChamSocRead])
def get_lich_su_cham_soc_by_hoc_sinh_id(thong_tin_hoc_sinh_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.get_lich_su_cham_soc_by_hoc_sinh_id(db, thong_tin_hoc_sinh_id)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc cho học sinh này")
        return JSONResponse(status_code=200, content={"message": "Lấy lịch sử chăm sóc thành công", "data": [r.dict() for r in result]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi truy vấn lịch sử chăm sóc: {str(e)}")


@router.put("/{cham_soc_id}", response_model=LichSuChamSocRead)
def update_lich_su_cham_soc(cham_soc_id: int, data: LichSuChamSocUpdate, db: Session = Depends(get_db)):
    try:
        result = crud.update_lich_su_cham_soc(db, cham_soc_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc")
        return JSONResponse(status_code=200, content={"message": "Cập nhật lịch sử chăm sóc thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật lịch sử chăm sóc: {str(e)}")


@router.delete("/{cham_soc_id}")
def delete_lich_su_cham_soc(cham_soc_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.soft_delete_lich_su_cham_soc(db, cham_soc_id)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy lịch sử chăm sóc")
        return JSONResponse(status_code=200, content={"message": "Đã xoá lịch sử chăm sóc thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá lịch sử chăm sóc: {str(e)}")

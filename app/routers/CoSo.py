from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import List

from app.database import get_db
from app.schemas.CoSo import CoSoCreate, CoSoRead, CoSoUpdate
from app.crud import CoSo as crud

router = APIRouter(
    prefix="/co_so",
    tags=["CoSo"]
)

@router.post("/", response_model=CoSoRead)
def create_co_so(data: CoSoCreate, db: Session = Depends(get_db)):
    try:
        result = crud.create_co_so(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo cơ sở thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo cơ sở: {str(e)}")


@router.get("/", response_model=List[CoSoRead])
def get_all_co_so(db: Session = Depends(get_db)):
    try:
        result = crud.get_all_co_so(db)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy cơ sở nào")
        return JSONResponse(status_code=200, content={"message": "Lấy danh sách cơ sở thành công", "data": [r.dict() for r in result]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách cơ sở: {str(e)}")


@router.put("/{co_so_id}", response_model=CoSoRead)
def update_co_so(co_so_id: int, data: CoSoUpdate, db: Session = Depends(get_db)):
    try:
        result = crud.update_co_so(db, co_so_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Cơ sở không tồn tại")
        return JSONResponse(status_code=200, content={"message": "Cập nhật cơ sở thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật cơ sở: {str(e)}")


@router.delete("/{co_so_id}")
def delete_co_so(co_so_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_co_so(db, co_so_id)
        if not result:
            raise HTTPException(status_code=404, detail="Cơ sở không tồn tại")
        return JSONResponse(status_code=200, content={"message": "Xoá cơ sở thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá cơ sở: {str(e)}")

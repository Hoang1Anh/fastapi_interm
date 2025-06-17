from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session

from app.database import get_db
from app.schemas.HocSinh import InsertHocSinh, HocSinhFilter
from app.crud import HocSinh as hoc_sinh_crud

router = APIRouter(prefix="/hoc_sinh", tags=["HocSinh"])

@router.post("/")
def create_hoc_sinh(data: InsertHocSinh, db: Session = Depends(get_db)):
    try:
        result = hoc_sinh_crud.create_hoc_sinh(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo học sinh thành công", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo học sinh: {str(e)}")


@router.post("/filter")
def filter_hoc_sinh(filter: HocSinhFilter, db: Session = Depends(get_db)):
    try:
        result = hoc_sinh_crud.get_all_hoc_sinh(db, filter)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy học sinh")
        return JSONResponse(status_code=200, content={"message": "Lọc danh sách học sinh thành công", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lọc học sinh: {str(e)}")


@router.put("/{user_id}")
def update_hoc_sinh(user_id: int, data: InsertHocSinh, db: Session = Depends(get_db)):
    try:
        result = hoc_sinh_crud.update_hoc_sinh(db, user_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy học sinh")
        return JSONResponse(status_code=200, content={"message": "Cập nhật học sinh thành công", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật học sinh: {str(e)}")


@router.delete("/{user_id}")
def delete_hoc_sinh(user_id: int, db: Session = Depends(get_db)):
    try:
        result = hoc_sinh_crud.soft_delete_hoc_sinh(db, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy học sinh hoặc đã xoá")
        return JSONResponse(status_code=200, content={"message": "Đã xoá học sinh thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá học sinh: {str(e)}")

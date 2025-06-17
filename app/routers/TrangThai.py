from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlmodel import Session
from app.schemas.TrangThai import TrangThaiCreate, TrangThaiRead, TrangThaiUpdate
from app.crud import TrangThai as crud
from app.database import get_db

router = APIRouter(
    prefix="/trang_thai",
    tags=["TrangThai"]
)

@router.post("/", response_model=TrangThaiRead)
def create_trang_thai(data: TrangThaiCreate, db: Session = Depends(get_db)):
    if not data.ten_trang_thai:
        raise HTTPException(status_code=400, detail="Tên trạng thái là bắt buộc")

    try:
        created = crud.create_trang_thai(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo trạng thái thành công", "data": created.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo trạng thái: {str(e)}")


@router.get("/", response_model=list[TrangThaiRead])
def get_all_trang_thai(db: Session = Depends(get_db)):
    try:
        result = crud.get_all_trang_thai(db)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy trạng thái nào")
        return JSONResponse(status_code=200, content={"message": "Lấy danh sách trạng thái thành công", "data": [r.dict() for r in result]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách trạng thái: {str(e)}")


@router.put("/{trang_thai_id}", response_model=TrangThaiRead)
def update_trang_thai(trang_thai_id: int, data: TrangThaiUpdate, db: Session = Depends(get_db)):
    if not trang_thai_id:
        raise HTTPException(status_code=400, detail="Thiếu ID trạng thái để cập nhật")

    try:
        result = crud.update_trang_thai(db, trang_thai_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Trạng thái không tồn tại")
        return JSONResponse(status_code=200, content={"message": "Cập nhật trạng thái thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật trạng thái: {str(e)}")


@router.delete("/{trang_thai_id}")
def delete_trang_thai(trang_thai_id: int, db: Session = Depends(get_db)):
    if not trang_thai_id:
        raise HTTPException(status_code=400, detail="Thiếu ID trạng thái để xoá")

    try:
        result = crud.soft_delete_trang_thai(db, trang_thai_id)
        if not result:
            raise HTTPException(status_code=404, detail="Trạng thái không tồn tại hoặc đã bị xoá")
        return JSONResponse(status_code=200, content={"message": "Xoá trạng thái thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá trạng thái: {str(e)}")


@router.patch("/change_status/{user_id}")
def change_status(user_id: int, status_id: int = Query(..., description="ID trạng thái mới"), db: Session = Depends(get_db)):
    if not user_id or not status_id:
        raise HTTPException(status_code=400, detail="Cần cung cấp user_id và status_id")

    try:
        user = crud.change_status(db, user_id, status_id)
        if not user:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng hoặc không thể cập nhật trạng thái")
        return JSONResponse(status_code=200, content={"message": "Cập nhật trạng thái người dùng thành công", "data": user.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi thay đổi trạng thái: {str(e)}")

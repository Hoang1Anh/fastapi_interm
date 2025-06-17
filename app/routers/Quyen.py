from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_db
from app.schemas.Quyen import QuyenRead, QuyenCreate, QuyenUpdate
from app.crud import Quyen as crud_quyen

router = APIRouter(prefix="/quyen", tags=["Quyen"])


@router.post("/", response_model=QuyenRead)
def create_quyen(quyen_data: QuyenCreate, db: Session = Depends(get_db)):
    try:
        return crud_quyen.create_quyen(db, quyen_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo quyền: {str(e)}")


@router.get("/", response_model=list[QuyenRead])
def get_all_quyen(db: Session = Depends(get_db)):
    try:
        return crud_quyen.get_all_quyen(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách quyền: {str(e)}")


@router.get("/{quyen_id}", response_model=QuyenRead)
def get_quyen_by_id(quyen_id: int, db: Session = Depends(get_db)):
    try:
        quyen = crud_quyen.get_quyen_by_id(db, quyen_id)
        if not quyen:
            raise HTTPException(status_code=404, detail="Không tìm thấy quyền")
        return quyen
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy quyền: {str(e)}")


@router.put("/{quyen_id}", response_model=QuyenRead)
def update_quyen(quyen_id: int, data: QuyenUpdate, db: Session = Depends(get_db)):
    try:
        quyen = crud_quyen.update_quyen(db, quyen_id, data)
        if not quyen:
            raise HTTPException(status_code=404, detail="Không tìm thấy quyền")
        return quyen
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật quyền: {str(e)}")


@router.delete("/{quyen_id}")
def delete_quyen(quyen_id: int, db: Session = Depends(get_db)):
    try:
        success = crud_quyen.soft_delete_quyen(db, quyen_id)
        if not success:
            raise HTTPException(status_code=404, detail="Không tìm thấy quyền")
        return {"message": "Đã xoá quyền thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá quyền: {str(e)}")

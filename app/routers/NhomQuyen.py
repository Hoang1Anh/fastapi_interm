from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from sqlmodel import Session
from app.schemas.NhomQuyen import NhomQuyenCreate, NhomQuyenRead, NhomQuyenUpdate
from app.schemas.QuyenCuaNhom import QuyenAssignRequest
from app.database import get_db
from app.crud import NhomQuyen as crud
from app.crud import QuyenCuaNhom as crud_quyen_nhom

router = APIRouter(prefix="/nhom_quyen", tags=["NhomQuyen"])

@router.post("/", response_model=NhomQuyenRead)
def create_nhom_quyen(data: NhomQuyenCreate, db: Session = Depends(get_db)):
    try:
        created = crud.create_nhom_quyen(db, data)
        return JSONResponse(status_code=200, content={"message": "Tạo nhóm quyền thành công", "data": created.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo nhóm quyền: {str(e)}")

@router.get("/", response_model=list[NhomQuyenRead])
def get_all_nhom_quyen(db: Session = Depends(get_db)):
    try:
        result = crud.get_all_nhom_quyen(db)
        if not result:
            raise HTTPException(status_code=404, detail="Không tìm thấy nhóm quyền nào")
        return JSONResponse(status_code=200, content={"message": "Lấy danh sách nhóm quyền thành công", "data": [r.dict() for r in result]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách nhóm quyền: {str(e)}")

@router.put("/{nhom_quyen_id}", response_model=NhomQuyenRead)
def update_nhom_quyen(nhom_quyen_id: int, data: NhomQuyenUpdate, db: Session = Depends(get_db)):
    try:
        result = crud.update_nhom_quyen(db, nhom_quyen_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Nhóm quyền không tồn tại")
        return JSONResponse(status_code=200, content={"message": "Cập nhật nhóm quyền thành công", "data": result.dict()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật nhóm quyền: {str(e)}")

@router.delete("/{nhom_quyen_id}")
def delete_nhom_quyen(nhom_quyen_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.soft_delete_nhom_quyen(db, nhom_quyen_id)
        if not result:
            raise HTTPException(status_code=404, detail="Nhóm quyền không tồn tại hoặc đã bị xoá")
        return JSONResponse(status_code=200, content={"message": "Đã xoá nhóm quyền thành công"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá nhóm quyền: {str(e)}")

@router.post("/gan_quyen")
def gan_quyen_cho_nhom(payload: QuyenAssignRequest, db: Session = Depends(get_db), request: Request = None):
    try:
        crud_quyen_nhom.assign_quyen_cho_nhom(db, payload.nhom_quyen_id, payload.quyen_ids)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Gán quyền cho nhóm thành công"}
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Lỗi khi gán quyền cho nhóm: {str(e)}")

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import List
from app.schemas.User import UserCreate, UserRead, UserUpdate
from app.crud import User as crud_user
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        created = crud_user.create_user(db, data)
        return JSONResponse(
            status_code=200,
            content={"message": "Tạo người dùng thành công", "data": created.dict()}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo người dùng: {str(e)}")

@router.get("/", response_model=List[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = crud_user.get_all_users(db)
        if not users:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng nào")
        return JSONResponse(
            status_code=200,
            content={
                "message": "Lấy danh sách người dùng thành công",
                "data": [u.dict() for u in users]
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy danh sách người dùng: {str(e)}")

@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    try:
        user = crud_user.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Người dùng không tồn tại")
        return JSONResponse(
            status_code=200,
            content={"message": "Lấy người dùng thành công", "data": user.dict()}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy người dùng: {str(e)}")

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    try:
        updated = crud_user.update_user(db, user_id, data)
        if not updated:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng để cập nhật")
        return JSONResponse(
            status_code=200,
            content={"message": "Cập nhật người dùng thành công", "data": updated.dict()}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật người dùng: {str(e)}")

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_user.soft_delete_user(db, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="Người dùng không tồn tại hoặc đã bị xoá")
        return JSONResponse(
            status_code=200,
            content={"message": "Đã xoá người dùng thành công"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xoá người dùng: {str(e)}")

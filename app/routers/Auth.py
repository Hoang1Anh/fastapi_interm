from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from app.models.User import User
from app.schemas.User import UserLogin, Token
from app.database import get_db
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, request: Request, session: Session = Depends(get_db)):
    try:
        user = session.exec(
            select(User).where(User.ten_dang_nhap == user_data.ten_dang_nhap)
        ).first()
        if not user or not verify_password(user_data.password, user.password):
            raise HTTPException(status_code=401, detail="Thông tin đăng nhập không hợp lệ")

        access_token = create_access_token(data={"sub": user.uuid})
        refresh_token = create_refresh_token(data={"sub": user.uuid})

        return JSONResponse(
            status_code=200,
            content={
                "message": "Đăng nhập thành công",
                "data": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "bearer"
                }
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi đăng nhập: {str(e)}")


@router.post("/refresh", response_model=Token)
def refresh_token(refresh_token: str):
    try:
        payload = decode_access_token(refresh_token)
        if not payload or payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Refresh token không hợp lệ")

        new_access_token = create_access_token(data={"sub": payload["sub"]})
        return JSONResponse(
            status_code=200,
            content={
                "message": "Làm mới token thành công",
                "data": {
                    "access_token": new_access_token,
                    "token_type": "bearer"
                }
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi làm mới token: {str(e)}")

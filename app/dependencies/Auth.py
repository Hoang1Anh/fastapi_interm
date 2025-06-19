from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordBearer
from app.database import get_session
from app.models.User import User
from app.auth import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")
    
    user = session.exec(select(User).where(User.uuid == payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="Người dùng không tồn tại")

    return user

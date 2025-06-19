from fastapi import Depends
from app.models.NhomQuyen import NhomQuyen
from app.models.QuyenCuaNhom import QuyenCuaNhom
from app.models.Quyen import Quyen
from sqlmodel import select

def KiemTraQuyen(ma_quyen: str):
    def checker(
        user: User = Depends(get_current_user),
        session: Session = Depends(get_session)
    ):
        # Truy vấn các quyền của nhóm mà user thuộc về
        stmt = (
            select(Quyen.Ma_quyen)
            .join(QuyenCuaNhom, Quyen.ID == QuyenCuaNhom.Quyen_id)
            .where(QuyenCuaNhom.Nhom_quyen_id == user.nhom_quyen_id)
        )
        result = session.exec(stmt).all()

        if ma_quyen not in result:
            raise HTTPException(status_code=403, detail="Không có quyền truy cập")
    return checker


# Sau thêm vào API dependencies=[Depends(require_permission("XEM_CO_SO"))]
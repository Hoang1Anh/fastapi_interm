from sqlmodel import Session, select
from datetime import datetime
from app.models.ThongTinNguoiDung import ThongTinNguoiDung
from app.models.ThongTinHocSinh import ThongTinHocSinh
from app.models.LichSuChamSoc import LichSuChamSoc
from app.schemas.HocSinh import InsertHocSinh, HocSinhFilter

def create_hoc_sinh(db: Session, data: InsertHocSinh):
    # Tạo người dùng
    nguoi_dung_data = data.nguoi_dung
    nguoi_dung = ThongTinNguoiDung(**nguoi_dung_data.dict())
    db.add(nguoi_dung)
    db.commit()
    db.refresh(nguoi_dung)

    # Tạo học sinh
    hoc_sinh_data = data.hoc_sinh
    hoc_sinh = ThongTinHocSinh(**hoc_sinh_data.dict(), thong_tin_id=nguoi_dung.id)
    db.add(hoc_sinh)
    db.commit()
    db.refresh(hoc_sinh)

    return {"message": "Thêm thành công", "user_id": nguoi_dung.id}

def get_all_hoc_sinh(db: Session, filter: HocSinhFilter):
    users_query = select(ThongTinNguoiDung)

    # Lọc theo keyword
    if filter.keyword:
        keyword_like = f"%{filter.keyword}%"
        users_query = users_query.where(
            or_(
                ThongTinNguoiDung.ho_ten.ilike(keyword_like),
                ThongTinNguoiDung.email.ilike(keyword_like),
                ThongTinNguoiDung.sdt.ilike(keyword_like),
            )
        )

    # Lọc theo năm sinh
    if filter.nam_sinh:
        year_start = datetime(filter.nam_sinh, 1, 1)
        year_end = datetime(filter.nam_sinh, 12, 31, 23, 59, 59)
        users_query = users_query.where(
            ThongTinNguoiDung.ngay_sinh.between(year_start, year_end)
        )

    users = db.exec(users_query).all()
    result = []

    for user in users:
        hoc_sinh = db.exec(
            select(ThongTinHocSinh).where(ThongTinHocSinh.thong_tin_id == user.id)
        ).first()

        cham_soc_list = []
        if hoc_sinh:
            cham_soc_query = select(LichSuChamSoc).where(
                LichSuChamSoc.thong_tin_hoc_sinh_id == hoc_sinh.id
            )

            # Lọc theo chăm sóc từ ngày đến ngày
            if filter.cham_soc_tu_ngay:
                cham_soc_query = cham_soc_query.where(
                    LichSuChamSoc.thoi_gian >= filter.cham_soc_tu_ngay
                )
            if filter.cham_soc_den_ngay:
                cham_soc_query = cham_soc_query.where(
                    LichSuChamSoc.thoi_gian <= filter.cham_soc_den_ngay
                )

            # Lọc theo nhân viên chăm sóc
            if filter.nhan_vien_id:
                cham_soc_query = cham_soc_query.where(
                    LichSuChamSoc.nhan_vien_id == filter.nhan_vien_id
                )

            cham_soc_list = db.exec(cham_soc_query).all()

        result.append({
            "NguoiDung": user.dict(),
            "HocSinh": hoc_sinh.dict() if hoc_sinh else None,
            "TrangThai": user.trang_thai.dict() if user.trang_thai else None,
            "CoSo": user.co_so.dict() if user.co_so else None,
            "LoaiNguoiDung": user.loai_nguoi_dung.dict() if user.loai_nguoi_dung else None,
            "LichSuChamSoc": [cs.dict() for cs in cham_soc_list]
        })

    return result

def update_hoc_sinh(db: Session, user_id: int, data: InsertHocSinh):
    nguoi_dung = db.get(ThongTinNguoiDung, user_id)
    if not nguoi_dung:
        return None

    nguoi_dung_data = data.nguoi_dung.dict(exclude_unset=True)
    for key, value in nguoi_dung_data.items():
        setattr(nguoi_dung, key, value)
    db.add(nguoi_dung)
    db.commit()
    db.refresh(nguoi_dung)

    hoc_sinh = db.exec(
        select(ThongTinHocSinh).where(ThongTinHocSinh.thong_tin_id == user_id)
    ).first()

    if hoc_sinh:
        hoc_sinh_data = data.hoc_sinh.dict(exclude_unset=True)
        for key, value in hoc_sinh_data.items():
            setattr(hoc_sinh, key, value)
        db.add(hoc_sinh)
        db.commit()
        db.refresh(hoc_sinh)

    return {"message": "Cập nhật thành công", "user_id": nguoi_dung.id}

def delete_hoc_sinh(db: Session, user_id: int):
    nguoi_dung = db.get(ThongTinNguoiDung, user_id)
    if not nguoi_dung:
        return None

    hoc_sinh = db.exec(
        select(ThongTinHocSinh).where(ThongTinHocSinh.thong_tin_id == user_id)
    ).first()

    if hoc_sinh:
        db.delete(hoc_sinh)

    db.delete(nguoi_dung)
    db.commit()
    return {"message": "Xoá thành công"}

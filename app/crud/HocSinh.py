from sqlmodel import Session, select, or_
from app.models.ThongTinNguoiDung import ThongTinNguoiDung
from app.models.ThongTinHocSinh import ThongTinHocSinh
from app.models.LichSuChamSoc import LichSuChamSoc
from app.schemas.HocSinh import InsertHocSinh, HocSinhFilter
from app import utils

def create_hoc_sinh(db: Session, data: InsertHocSinh):
    nguoi_dung_data = data.nguoi_dung
    nguoi_dung = ThongTinNguoiDung(**nguoi_dung_data.dict())
    db.add(nguoi_dung)
    db.commit()
    db.refresh(nguoi_dung)

    hoc_sinh_data = data.hoc_sinh
    hoc_sinh = ThongTinHocSinh(**hoc_sinh_data.dict(), thong_tin_id=nguoi_dung.id)
    db.add(hoc_sinh)
    db.commit()
    db.refresh(hoc_sinh)

    return {"message": "Thêm thành công", "user_id": nguoi_dung.id}


def get_all_hoc_sinh(db: Session, filter: HocSinhFilter):
    query = select(ThongTinNguoiDung).where(ThongTinNguoiDung.deleted_at.is_(None))

    if filter.keyword:
        keyword = f"%{filter.keyword}%"
        query = query.where(
            or_(
                ThongTinNguoiDung.ho_ten.ilike(keyword),
                ThongTinNguoiDung.email.ilike(keyword),
                ThongTinNguoiDung.sdt.ilike(keyword)
            )
        )

    if filter.nam_sinh:
        from datetime import datetime
        start = datetime(filter.nam_sinh, 1, 1)
        end = datetime(filter.nam_sinh, 12, 31, 23, 59, 59)
        query = query.where(ThongTinNguoiDung.ngay_sinh.between(start, end))

    users = db.exec(query).all()
    results = []

    for user in users:
        hoc_sinh = db.exec(
            select(ThongTinHocSinh).where(
                ThongTinHocSinh.thong_tin_id == user.id,
                ThongTinHocSinh.deleted_at.is_(None)
            )
        ).first()

        cham_soc_list = []
        if hoc_sinh:
            cs_query = select(LichSuChamSoc).where(
                LichSuChamSoc.thong_tin_hoc_sinh_id == hoc_sinh.id,
                LichSuChamSoc.deleted_at.is_(None)
            )
            if filter.cham_soc_tu_ngay:
                cs_query = cs_query.where(LichSuChamSoc.thoi_gian >= filter.cham_soc_tu_ngay)
            if filter.cham_soc_den_ngay:
                cs_query = cs_query.where(LichSuChamSoc.thoi_gian <= filter.cham_soc_den_ngay)
            if filter.nhan_vien_id:
                cs_query = cs_query.where(LichSuChamSoc.nhan_vien_id == filter.nhan_vien_id)

            cham_soc_list = db.exec(cs_query).all()

        results.append({
            "NguoiDung": user.dict(),
            "HocSinh": hoc_sinh.dict() if hoc_sinh else None,
            "TrangThai": user.trang_thai.dict() if user.trang_thai else None,
            "CoSo": user.co_so.dict() if user.co_so else None,
            "LoaiNguoiDung": user.loai_nguoi_dung.dict() if user.loai_nguoi_dung else None,
            "LichSuChamSoc": [cs.dict() for cs in cham_soc_list]
        })

    return results


def update_hoc_sinh(db: Session, user_id: int, data: InsertHocSinh):
    nguoi_dung = db.get(ThongTinNguoiDung, user_id)
    if not nguoi_dung or nguoi_dung.deleted_at is not None:
        return None

    for key, value in data.nguoi_dung.dict(exclude_unset=True).items():
        setattr(nguoi_dung, key, value)
    db.add(nguoi_dung)
    db.commit()
    db.refresh(nguoi_dung)

    hoc_sinh = db.exec(
        select(ThongTinHocSinh).where(
            ThongTinHocSinh.thong_tin_id == user_id,
            ThongTinHocSinh.deleted_at.is_(None)
        )
    ).first()

    if hoc_sinh:
        for key, value in data.hoc_sinh.dict(exclude_unset=True).items():
            setattr(hoc_sinh, key, value)
        db.add(hoc_sinh)
        db.commit()
        db.refresh(hoc_sinh)

    return {"message": "Cập nhật thành công", "user_id": nguoi_dung.id}


def delete_hoc_sinh(db: Session, user_id: int):
    nguoi_dung = db.get(ThongTinNguoiDung, user_id)
    if not nguoi_dung or nguoi_dung.deleted_at is not None:
        return None

    now = utils.get_current_time()

    hoc_sinh = db.exec(
        select(ThongTinHocSinh).where(
            ThongTinHocSinh.thong_tin_id == user_id,
            ThongTinHocSinh.deleted_at.is_(None)
        )
    ).first()

    if hoc_sinh:
        hoc_sinh.deleted_at = now
        db.add(hoc_sinh)

    nguoi_dung.deleted_at = now
    db.add(nguoi_dung)

    db.commit()
    return {"message": "Đã đánh dấu xoá học sinh thành công"}

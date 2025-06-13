from .ThongTinNguoiDung import ThongTinNguoiDung
from .ThongTinHocSinh import ThongTinHocSinh
from .LichSuChamSoc import LichSuChamSoc
from .CoSo import CoSo
from .LoaiNguoiDung import LoaiNguoiDung
from .TrangThai import TrangThai

# Khởi tạo forward references để đảm bảo SQLModel hiểu các mối quan hệ
ThongTinNguoiDung.update_forward_refs()
ThongTinHocSinh.update_forward_refs()
LichSuChamSoc.update_forward_refs()
CoSo.update_forward_refs()
LoaiNguoiDung.update_forward_refs()
TrangThai.update_forward_refs()

__all__ = [
    "ThongTinNguoiDung",
    "ThongTinHocSinh",
    "LichSuChamSoc",
    "CoSo",
    "LoaiNguoiDung",
    "TrangThai"
]
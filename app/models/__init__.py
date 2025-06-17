from .ThongTinNguoiDung import ThongTinNguoiDung
from .ThongTinHocSinh import ThongTinHocSinh
from .LichSuChamSoc import LichSuChamSoc
from .CoSo import CoSo
from .LoaiNguoiDung import LoaiNguoiDung
from .TrangThai import TrangThai
from .LichSuHeThong import LichSuHeThong
from .User import User
from .NhomQuyen import NhomQuyen
from .Quyen import Quyen
from .QuyenCuaNhom import QuyenCuaNhom

# Khởi tạo forward references
ThongTinNguoiDung.update_forward_refs()
ThongTinHocSinh.update_forward_refs()
LichSuChamSoc.update_forward_refs()
CoSo.update_forward_refs()
LoaiNguoiDung.update_forward_refs()
TrangThai.update_forward_refs()
User.update_forward_refs()
NhomQuyen.update_forward_refs()
Quyen.update_forward_refs()
QuyenCuaNhom.update_forward_refs()

__all__ = [
    "ThongTinNguoiDung",
    "ThongTinHocSinh",
    "LichSuChamSoc",
    "LichSuHeThong",
    "CoSo",
    "LoaiNguoiDung",
    "TrangThai",
    "User",
    "NhomQuyen",
    "Quyen",
    "QuyenCuaNhom"
]

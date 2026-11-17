from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    ma: str
    ten: str
    tac_gia: str
    the_loai: str
    nam: int
    nxb: str
    so_luong: int
    dang_muon: int = 0

    def __post_init__(self):
        """Kiểm tra dữ liệu để mỗi đối tượng Book luôn hợp lệ."""
        self.ma = str(self.ma).strip()
        self.ten = str(self.ten).strip()
        self.tac_gia = str(self.tac_gia).strip()
        self.the_loai = str(self.the_loai).strip()
        self.nxb = str(self.nxb).strip()

        if not all([self.ma, self.ten, self.tac_gia, self.the_loai, self.nxb]):
            raise ValueError("Thông tin sách không được để trống.")

        if not isinstance(self.nam, int) or not 1 <= self.nam <= datetime.now().year:
            raise ValueError("Năm xuất bản không hợp lệ.")

        if not isinstance(self.so_luong, int) or self.so_luong < 0:
            raise ValueError("Số lượng phải là số nguyên không âm.")

        if not isinstance(self.dang_muon, int) or not 0 <= self.dang_muon <= self.so_luong:
            raise ValueError("Số lượng đang mượn không hợp lệ.")

    def so_luong_con_lai(self):
        return self.so_luong - self.dang_muon

    def hien_thi(self):
        print(
            f"{self.ma:<12}{self.ten:<30}{self.tac_gia:<22}"
            f"{self.the_loai:<18}{self.nam:<8}{self.nxb:<22}"
            f"{self.so_luong:<10}{self.dang_muon:<12}"
            f"{self.so_luong_con_lai():<10}"
        )

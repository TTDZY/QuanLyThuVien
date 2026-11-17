from models import Book
from utils import (
    nhap_chuoi_khong_rong, nhap_so_nguyen, nhap_nam,
    nhap_ma_sach, xac_nhan, in_duong_ke
)


class BookManager:
    def __init__(self):
        self.books = []

    def tim_theo_ma(self, ma):
        ma = ma.strip().casefold()
        for book in self.books:
            if book.ma.casefold() == ma:
                return book
        return None

    def kiem_tra_ma_trung(self, ma):
        return self.tim_theo_ma(ma) is not None

    def them_sach(self):
        print("\n========== THÊM SÁCH ==========")
        ma = nhap_ma_sach("Nhập mã sách: ")
        if self.kiem_tra_ma_trung(ma):
            print("Mã sách đã tồn tại!")
            return

        ten = nhap_chuoi_khong_rong("Nhập tên sách: ")
        tac_gia = nhap_chuoi_khong_rong("Nhập tác giả: ")
        the_loai = nhap_chuoi_khong_rong("Nhập thể loại: ")
        nam = nhap_nam("Nhập năm xuất bản: ")
        nxb = nhap_chuoi_khong_rong("Nhập nhà xuất bản: ")
        so_luong = nhap_so_nguyen("Nhập số lượng: ", min_value=0)

        self.books.append(Book(ma, ten, tac_gia, the_loai, nam, nxb, so_luong))
        print("Thêm sách thành công!")

    def hien_thi_tieu_de(self):
        in_duong_ke()
        print(
            f"{'Mã':<12}{'Tên sách':<30}{'Tác giả':<22}"
            f"{'Thể loại':<18}{'Năm':<8}{'NXB':<22}"
            f"{'SL':<10}{'Đang mượn':<12}{'Còn lại':<10}"
        )
        in_duong_ke()

    def hien_thi_danh_sach(self):
        print("\n========== DANH SÁCH SÁCH ==========")
        if not self.books:
            print("Danh sách sách đang trống.")
            return
        self.hien_thi_tieu_de()
        for book in self.books:
            book.hien_thi()
        in_duong_ke()

    def cap_nhat_sach(self):
        print("\n========== CẬP NHẬT SÁCH ==========")
        ma = nhap_ma_sach("Nhập mã sách cần cập nhật: ")
        book = self.tim_theo_ma(ma)
        if book is None:
            print("Không tìm thấy sách.")
            return

        print("Nhập thông tin mới (mã sách được giữ nguyên):")
        ten = nhap_chuoi_khong_rong("Tên sách mới: ")
        tac_gia = nhap_chuoi_khong_rong("Tác giả mới: ")
        the_loai = nhap_chuoi_khong_rong("Thể loại mới: ")
        nam = nhap_nam("Năm xuất bản mới: ")
        nxb = nhap_chuoi_khong_rong("Nhà xuất bản mới: ")

        while True:
            so_luong = nhap_so_nguyen("Số lượng mới: ", min_value=0)
            if so_luong < book.dang_muon:
                print(f"Số lượng phải >= số đang mượn ({book.dang_muon}).")
            else:
                break

        book.ten = ten
        book.tac_gia = tac_gia
        book.the_loai = the_loai
        book.nam = nam
        book.nxb = nxb
        book.so_luong = so_luong
        print("Cập nhật sách thành công!")

    def xoa_sach(self):
        print("\n========== XÓA SÁCH ==========")
        ma = nhap_ma_sach("Nhập mã sách cần xóa: ")
        book = self.tim_theo_ma(ma)
        if book is None:
            print("Không tìm thấy sách.")
            return
        if book.dang_muon > 0:
            print(f"Không thể xóa vì đang có {book.dang_muon} cuốn được mượn.")
            return
        if xac_nhan("Bạn có chắc chắn muốn xóa? (Y/N): "):
            self.books.remove(book)
            print("Xóa sách thành công!")
        else:
            print("Đã hủy thao tác xóa.")

    def tim_kiem_ma(self):
        ma = nhap_ma_sach("Nhập mã sách: ")
        book = self.tim_theo_ma(ma)
        self.hien_thi_ket_qua([book] if book else [], "TÌM KIẾM THEO MÃ")

    def tim_kiem_ten(self):
        tu_khoa = nhap_chuoi_khong_rong("Nhập tên sách cần tìm: ").casefold()
        ket_qua = [b for b in self.books if tu_khoa in b.ten.casefold()]
        self.hien_thi_ket_qua(ket_qua, "TÌM KIẾM THEO TÊN")

    def tim_kiem_tac_gia(self):
        tu_khoa = nhap_chuoi_khong_rong("Nhập tên tác giả cần tìm: ").casefold()
        ket_qua = [b for b in self.books if tu_khoa in b.tac_gia.casefold()]
        self.hien_thi_ket_qua(ket_qua, "TÌM KIẾM THEO TÁC GIẢ")

    def tim_kiem_the_loai(self):
        tu_khoa = nhap_chuoi_khong_rong("Nhập thể loại cần tìm: ").casefold()
        ket_qua = [b for b in self.books if tu_khoa in b.the_loai.casefold()]
        self.hien_thi_ket_qua(ket_qua, "TÌM KIẾM THEO THỂ LOẠI")

    def hien_thi_ket_qua(self, ket_qua, tieu_de):
        print(f"\n========== {tieu_de} ==========")
        if not ket_qua:
            print("Không tìm thấy sách phù hợp.")
            return
        self.hien_thi_tieu_de()
        for book in ket_qua:
            book.hien_thi()
        in_duong_ke()

    def menu_tim_kiem(self):
        while True:
            print("\n========== TÌM KIẾM ==========")
            print("1. Tìm theo mã sách")
            print("2. Tìm theo tên sách")
            print("3. Tìm theo tác giả")
            print("4. Tìm theo thể loại")
            print("0. Quay lại")
            lua_chon = input("Lựa chọn: ").strip()

            if lua_chon == "1":
                self.tim_kiem_ma()
            elif lua_chon == "2":
                self.tim_kiem_ten()
            elif lua_chon == "3":
                self.tim_kiem_tac_gia()
            elif lua_chon == "4":
                self.tim_kiem_the_loai()
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ!")

    def sap_xep(self):
        if not self.books:
            print("Danh sách sách đang trống.")
            return

        print("\n========== SẮP XẾP ==========")
        print("1. Theo tên sách")
        print("2. Theo năm xuất bản")
        print("3. Theo số lượng")
        print("0. Quay lại")
        lua_chon = input("Lựa chọn: ").strip()

        if lua_chon == "0":
            return
        if lua_chon not in ("1", "2", "3"):
            print("Lựa chọn không hợp lệ!")
            return

        print("\n1. Tăng dần")
        print("2. Giảm dần")
        thu_tu = input("Lựa chọn: ").strip()
        if thu_tu not in ("1", "2"):
            print("Lựa chọn không hợp lệ!")
            return

        key_map = {
            "1": lambda b: b.ten.casefold(),
            "2": lambda b: b.nam,
            "3": lambda b: b.so_luong,
        }
        self.books.sort(key=key_map[lua_chon], reverse=(thu_tu == "2"))
        print("Sắp xếp thành công!")
        self.hien_thi_danh_sach()

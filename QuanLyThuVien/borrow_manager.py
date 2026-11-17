from utils import nhap_ma_sach, nhap_so_nguyen


class BorrowManager:
    def __init__(self, book_manager):
        self.book_manager = book_manager

    def muon_sach(self):
        print("\n========== MƯỢN SÁCH ==========")
        ma = nhap_ma_sach("Nhập mã sách muốn mượn: ")
        book = self.book_manager.tim_theo_ma(ma)
        if book is None:
            print("Sách không tồn tại.")
            return

        con_lai = book.so_luong_con_lai()
        print(f"Tên sách: {book.ten}")
        print(f"Số lượng hiện có: {con_lai}")
        if con_lai <= 0:
            print("Sách đã hết, không thể cho mượn.")
            return

        so_luong = nhap_so_nguyen(
            "Nhập số lượng muốn mượn: ", min_value=1, max_value=con_lai
        )
        book.dang_muon += so_luong
        print(f"Mượn thành công {so_luong} cuốn sách '{book.ten}'.")
        print(f"Số lượng còn lại: {book.so_luong_con_lai()}")

    def tra_sach(self):
        print("\n========== TRẢ SÁCH ==========")
        ma = nhap_ma_sach("Nhập mã sách muốn trả: ")
        book = self.book_manager.tim_theo_ma(ma)
        if book is None:
            print("Sách không tồn tại.")
            return
        if book.dang_muon <= 0:
            print("Sách này hiện không có sách đang được mượn.")
            return

        print(f"Tên sách: {book.ten}")
        print(f"Số lượng đang mượn: {book.dang_muon}")
        so_luong = nhap_so_nguyen(
            "Nhập số lượng muốn trả: ", min_value=1, max_value=book.dang_muon
        )
        book.dang_muon -= so_luong
        print(f"Trả thành công {so_luong} cuốn sách '{book.ten}'.")
        print(f"Số lượng hiện có: {book.so_luong_con_lai()}")

from collections import Counter


class Statistics:
    def __init__(self, book_manager):
        self.book_manager = book_manager

    def tong_so_dau_sach(self):
        return len(self.book_manager.books)

    def tong_so_sach(self):
        return sum(book.so_luong for book in self.book_manager.books)

    def tong_so_sach_dang_muon(self):
        return sum(book.dang_muon for book in self.book_manager.books)

    def sach_so_luong_lon_nhat(self):
        if not self.book_manager.books:
            return None
        return max(self.book_manager.books, key=lambda b: b.so_luong)

    def sach_xuat_ban_gan_nhat(self):
        if not self.book_manager.books:
            return None
        return max(self.book_manager.books, key=lambda b: b.nam)

    def thong_ke_the_loai(self):
        """Tổng số cuốn sách theo từng thể loại."""
        ket_qua = Counter()
        for book in self.book_manager.books:
            ket_qua[book.the_loai] += book.so_luong
        return ket_qua

    def thong_ke_dau_sach_theo_the_loai(self):
        """Số đầu sách (số mã sách) theo từng thể loại."""
        ket_qua = Counter()
        for book in self.book_manager.books:
            ket_qua[book.the_loai] += 1
        return ket_qua

    def hien_thi_thong_ke(self):
        print("\n" + "=" * 60)
        print("                 THỐNG KÊ THƯ VIỆN")
        print("=" * 60)
        if not self.book_manager.books:
            print("Danh sách sách đang trống.")
            return

        print(f"\n1. Tổng số đầu sách: {self.tong_so_dau_sach()}")
        print(f"2. Tổng số sách trong kho: {self.tong_so_sach()}")
        print(f"3. Tổng số sách đang được mượn: {self.tong_so_sach_dang_muon()}")

        sach_max = self.sach_so_luong_lon_nhat()
        print("\n4. Sách có số lượng lớn nhất:")
        print(f"   - Mã: {sach_max.ma}")
        print(f"   - Tên: {sach_max.ten}")
        print(f"   - Số lượng: {sach_max.so_luong}")

        sach_moi = self.sach_xuat_ban_gan_nhat()
        print("\n5. Sách xuất bản gần đây nhất:")
        print(f"   - Mã: {sach_moi.ma}")
        print(f"   - Tên: {sach_moi.ten}")
        print(f"   - Năm: {sach_moi.nam}")

        print("\n6. Thống kê theo thể loại:")
        for the_loai, so_cuon in self.thong_ke_the_loai().items():
            so_dau_sach = self.thong_ke_dau_sach_theo_the_loai()[the_loai]
            print(f"   - {the_loai}: {so_dau_sach} đầu sách, {so_cuon} cuốn")

        print("\n" + "=" * 60)

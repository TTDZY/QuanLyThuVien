import os

from book_manager import BookManager
from borrow_manager import BorrowManager
from statistics import Statistics
from file_manager import FileManager
from utils import xac_nhan


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "books.txt")


def hien_thi_menu():
    print("\n" + "=" * 50)
    print("              QUẢN LÝ THƯ VIỆN")
    print("=" * 50)
    print("1. Thêm sách")
    print("2. Hiển thị danh sách")
    print("3. Cập nhật sách")
    print("4. Xóa sách")
    print("5. Tìm kiếm")
    print("6. Sắp xếp")
    print("7. Mượn sách")
    print("8. Trả sách")
    print("9. Thống kê")
    print("10. Lưu dữ liệu")
    print("11. Đọc dữ liệu")
    print("0. Thoát")
    print("=" * 50)


def khoi_tao():
    book_manager = BookManager()
    borrow_manager = BorrowManager(book_manager)
    statistics = Statistics(book_manager)
    file_manager = FileManager(DATA_FILE)
    return book_manager, borrow_manager, statistics, file_manager


def main():
    book_manager, borrow_manager, statistics, file_manager = khoi_tao()

    du_lieu = file_manager.doc_du_lieu()
    book_manager.books = du_lieu if du_lieu is not None else []

    while True:
        hien_thi_menu()
        lua_chon = input("Lựa chọn: ").strip()

        if lua_chon == "1":
            book_manager.them_sach()
        elif lua_chon == "2":
            book_manager.hien_thi_danh_sach()
        elif lua_chon == "3":
            book_manager.cap_nhat_sach()
        elif lua_chon == "4":
            book_manager.xoa_sach()
        elif lua_chon == "5":
            book_manager.menu_tim_kiem()
        elif lua_chon == "6":
            book_manager.sap_xep()
        elif lua_chon == "7":
            borrow_manager.muon_sach()
        elif lua_chon == "8":
            borrow_manager.tra_sach()
        elif lua_chon == "9":
            statistics.hien_thi_thong_ke()
        elif lua_chon == "10":
            file_manager.luu_du_lieu(book_manager.books)
        elif lua_chon == "11":
            if xac_nhan("Đọc lại dữ liệu sẽ thay thế danh sách hiện tại. Tiếp tục? (Y/N): "):
                du_lieu = file_manager.doc_du_lieu()
                # Không xóa dữ liệu đang làm việc nếu file gặp lỗi đọc.
                if du_lieu is not None:
                    book_manager.books = du_lieu
        elif lua_chon == "0":
            if xac_nhan("Bạn có muốn lưu dữ liệu trước khi thoát? (Y/N): "):
                file_manager.luu_du_lieu(book_manager.books)
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nChương trình đã được dừng.")

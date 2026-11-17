import csv
import os
from datetime import datetime

from models import Book


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def luu_du_lieu(self, books):
        try:
            folder = os.path.dirname(self.file_path)
            if folder:
                os.makedirs(folder, exist_ok=True)

            # CSV có quoting nên nội dung chứa dấu | hoặc dấu ngoặc kép vẫn lưu đúng.
            with open(self.file_path, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file, delimiter="|", quoting=csv.QUOTE_MINIMAL)
                for book in books:
                    writer.writerow([
                        book.ma, book.ten, book.tac_gia, book.the_loai,
                        book.nam, book.nxb, book.so_luong, book.dang_muon
                    ])
            print("Lưu dữ liệu thành công!")
            return True
        except PermissionError:
            print("Không có quyền ghi file.")
        except OSError as e:
            print(f"Không thể lưu file: {e}")
        return False

    def doc_du_lieu(self):
        books = []
        ma_da_co = set()

        if not os.path.exists(self.file_path):
            print("File dữ liệu chưa tồn tại. Sử dụng danh sách rỗng.")
            return books

        try:
            with open(self.file_path, "r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file, delimiter="|")
                for line_number, parts in enumerate(reader, start=1):
                    if not parts or all(not str(part).strip() for part in parts):
                        continue
                    try:
                        if len(parts) != 8:
                            raise ValueError("sai định dạng, cần đúng 8 trường")

                        ma, ten, tac_gia, the_loai = [part.strip() for part in parts[:4]]
                        nam = int(parts[4])
                        nxb = parts[5].strip()
                        so_luong = int(parts[6])
                        dang_muon = int(parts[7])

                        if ma.casefold() in ma_da_co:
                            raise ValueError("mã sách bị trùng")

                        book = Book(
                            ma, ten, tac_gia, the_loai,
                            nam, nxb, so_luong, dang_muon
                        )
                        books.append(book)
                        ma_da_co.add(ma.casefold())
                    except (ValueError, TypeError) as e:
                        print(f"Bỏ qua dòng {line_number}: {e}")

            print(f"Đọc dữ liệu thành công! Có {len(books)} đầu sách.")
            return books
        except PermissionError:
            print("Không có quyền đọc file.")
        except (OSError, UnicodeError, csv.Error) as e:
            print(f"Không thể đọc file: {e}")
        return None

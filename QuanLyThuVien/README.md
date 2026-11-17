# QUẢN LÝ THƯ VIỆN BẰNG PYTHON

## 1. Giới thiệu
Chương trình quản lý thư viện bằng Python, chạy trên giao diện Console.
Chương trình hỗ trợ thêm, hiển thị, cập nhật, xóa, tìm kiếm, sắp xếp, mượn,
trả, thống kê và lưu/đọc dữ liệu TXT.

## 2. Yêu cầu môi trường
- Python 3.8 trở lên.
- Windows, Linux hoặc macOS.
- Không cần cài đặt thư viện bên ngoài.

## 3. Cấu trúc thư mục
```text
QuanLyThuVien/
├── main.py              # Chương trình chính, hiển thị menu và điều khiển các chức năng
├── models.py            # Khai báo lớp Book, lưu trữ và quản lý thông tin sách
├── book_manager.py      # Quản lý sách: thêm, sửa, xóa, tìm kiếm và sắp xếp
├── borrow_manager.py    # Xử lý nghiệp vụ mượn sách và trả sách
├── statistics.py        # Thống kê số lượng sách, sách đang mượn và thống kê theo thể loại
├── file_manager.py      # Đọc và ghi dữ liệu sách từ/đến file TXT
├── utils.py             # Các hàm tiện ích: nhập liệu, kiểm tra dữ liệu và xác nhận thao tác
├── README.md            # Tài liệu hướng dẫn cài đặt, chạy và sử dụng chương trình
└── data/
    └── books.txt        # File lưu trữ dữ liệu sách của thư viện
```

## 4. Cách chạy
1. Mở Terminal hoặc Command Prompt tại thư mục `QuanLyThuVien`.
2. Chạy lệnh:

```bash
python main.py
```

Nếu máy dùng lệnh `py` trên Windows, có thể chạy `py main.py`.

## 5. Định dạng dữ liệu
Dữ liệu được lưu trong `data/books.txt`, mỗi dòng tương ứng một đầu sách,
gồm 8 trường: mã, tên, tác giả, thể loại, năm xuất bản, nhà xuất bản,
số lượng và số lượng đang mượn. Dấu phân cách là `|`.

Chương trình sử dụng cơ chế CSV quoting để xử lý trường dữ liệu có chứa
ký tự phân cách hoặc dấu ngoặc kép.

## 6. Chức năng
- Quản lý sách: thêm, hiển thị, cập nhật, xóa.
- Tìm kiếm theo mã, tên, tác giả, thể loại.
- Sắp xếp theo tên, năm xuất bản, số lượng; tăng hoặc giảm dần.
- Mượn và trả sách, không cho mượn vượt số lượng còn.
- Thống kê số đầu sách, tổng số cuốn, sách có số lượng lớn nhất,
  sách xuất bản gần đây nhất và thống kê theo thể loại.
- Đọc dữ liệu khi khởi động; lưu hoặc đọc lại theo menu.

## 7. Lưu ý
Khi thêm hoặc thay đổi dữ liệu, hãy chọn chức năng **10. Lưu dữ liệu**
hoặc đồng ý lưu khi thoát để dữ liệu được ghi xuống file.

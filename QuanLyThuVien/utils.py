from datetime import datetime


def nhap_chuoi_khong_rong(thong_bao):
    while True:
        gia_tri = input(thong_bao).strip()
        if gia_tri:
            return gia_tri
        print("Không được để trống. Vui lòng nhập lại!")


def nhap_ma_sach(thong_bao):
    while True:
        ma = input(thong_bao).strip()
        if ma:
            return ma
        print("Mã sách không được để trống.")


def nhap_so_nguyen(thong_bao, min_value=None, max_value=None):
    while True:
        try:
            gia_tri = int(input(thong_bao).strip())
            if min_value is not None and gia_tri < min_value:
                print(f"Giá trị phải lớn hơn hoặc bằng {min_value}.")
                continue
            if max_value is not None and gia_tri > max_value:
                print(f"Giá trị phải nhỏ hơn hoặc bằng {max_value}.")
                continue
            return gia_tri
        except ValueError:
            print("Dữ liệu không hợp lệ! Vui lòng nhập số nguyên.")


def nhap_nam(thong_bao):
    return nhap_so_nguyen(
        thong_bao,
        min_value=1,
        max_value=datetime.now().year
    )


def xac_nhan(thong_bao):
    while True:
        lua_chon = input(thong_bao).strip().lower()
        if lua_chon in ("y", "yes", "c", "co", "có"):
            return True
        if lua_chon in ("n", "no", "k", "khong", "không"):
            return False
        print("Vui lòng nhập Y hoặc N.")


def in_duong_ke():
    print("=" * 150)

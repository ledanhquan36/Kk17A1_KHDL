# 10.1
from numbers import Number

def tim_gia_tri_nho_nhat_lon_nhat(lst):
    if all(isinstance(x, Number) for x in lst):
        return min(lst), max(lst)
    else:
        return "Danh sách chứa các phần tử không phải là số"

danh_sach_so = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = tim_gia_tri_nho_nhat_lon_nhat(danh_sach_so)
print("Giá trị nhỏ nhất là:", min_value)
print("Giá trị lớn nhất là:", max_value)


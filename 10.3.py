from numbers import Number

def tinh_gia_tri_S(x, n):
    if isinstance(x, Number) and isinstance(n, Number):
        return pow(x**2 + 1, n)
    else:
        return "Đầu vào không phải là số"

x = 2
n = 3
S = tinh_gia_tri_S(x, n)
print("Giá trị của biểu thức S = (x^2 + 1)^n là:", S)

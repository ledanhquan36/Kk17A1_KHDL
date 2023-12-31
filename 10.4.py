from numbers import Number

def tinh_gia_tri_A(x, n):
    if isinstance(x, Number) and isinstance(n, Number):
        term1 = pow(x**2 + x + 1, n)
        term2 = pow(x**2 - x + 1, n)
        return term1 + term2
    else:
        return "Đầu vào không phải là số"

x = 2
n = 3
A = tinh_gia_tri_A(x, n)
print("Giá trị của biểu thức A = (x^2 + x + 1)^n + (x^2 - x + 1)^n là:", A)

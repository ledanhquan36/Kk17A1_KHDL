a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))
c = float(input("Nhập số thứ ba (c): "))
d = float(input("Nhập số thứ tư (d): "))
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if b < min:
    b = min
if c < min:
    c = min
if d < min:
    d = min
print(f"Số lớn nhất là {max}")
print(f"Số nhỏ nhât là {min}")
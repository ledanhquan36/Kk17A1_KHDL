import math

# Nhập vào các hệ số a, b, c từ shell
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))

# Tính delta
delta = b**2 - 4*a*c

# Kiểm tra điều kiện để giải phương trình
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm")

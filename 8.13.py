n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng các số lẻ nhỏ hơn hoặc bằng n (A)
A = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        A += i

# Tính tổng các số chẵn nhỏ hơn hoặc bằng n (B)
B = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        B += i

# Tính tích của các số từ 1 đến n (C)
C = 1
for i in range(1, n + 1):
    C *= i

# Tính tích của các số chia hết cho 3 nhỏ hơn hoặc bằng n (D)
D = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        D *= i

# Tính tổng các số nguyên tố nhỏ hơn hoặc bằng n (E)
E = 0
for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        E += i

# Tính tổng chuỗi đan dấu (F)
F = ""
for i in range(1, n):
    F += str(i) + "-"
F += str(n)

print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
print("E = ", E)
print("F = ", F)

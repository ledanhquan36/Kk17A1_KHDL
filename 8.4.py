#tính diệnt ích tam giác bằng công thức herong
import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
#tính nửa chu vi p, p=((a+b+c)/2)
p = (a+b+c)/2
#tính S
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác theo công thức herong là: ", S)
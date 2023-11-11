m = eval(input("Nhập giá trị m: "))
n = eval(input("Nhập giá trị n: "))
if n <= m:
   print("Vui lòng nhập giá trị m nhỏ hơn n")
else:
      print(f"các số chia hết trong khoảng từ {m} đến {n} là :")
      for x in range(1 , n+1):
         if x % m == 0:
            print(x)

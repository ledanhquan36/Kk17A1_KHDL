#kiểm tra năm nhuận
nam_nhuan = int(input("Nhập năm: "))
if (nam_nhuan % 4 ==0 and nam_nhuan % 100 !=0) or (nam_nhuan % 400 ==0):
    print("Năm", nam_nhuan, "là năm nhuận")
else:
    print("Năm", nam_nhuan, "không là năm nhuận")
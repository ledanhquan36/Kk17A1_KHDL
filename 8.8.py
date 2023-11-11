gia_phong = [1260000, 1550000, 1830000, 1830000, 2120000, 2120000, 2540000, 4800000]
loai_phong = int(input("Nhập số phòng(1-8): "))
so_dem = int(input("Nhập số đêm ở resort: "))
if loai_phong < 1 or loai_phong > 8:
    print("số phòng không hợp lệ")
else:    
    gia_moi_dem = gia_phong[loai_phong - 1]
    if so_dem == 1:
        print("Số tiền cần thanh toán: ", gia_moi_dem, "VND")
    elif so_dem >= 2 and so_dem <= 3:
        gia_giam_25 = gia_moi_dem * 0.75
        print("Số tiền cần thanh toán: ", so_dem * gia_giam_25, "VND")
    elif so_dem >= 4:
        gia_giam_30 = gia_moi_dem * 0.7
        print("Số tiền cần thanh toán: ", so_dem * gia_giam_30, "VND")
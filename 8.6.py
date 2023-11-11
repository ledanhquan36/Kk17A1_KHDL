loai_xe = int(input("Nhập loại xe(4 hoặc 7 chỗ): "))
so_km = float(input("Nhấp số km: "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))
if loai_xe == 4:
    gia_mo_cua=11000
    km_pham_vi_20 = 20
    gia_km_20 = 12100
    gia_km_21_tro_di = 10000
     
    if so_km <= 8:
        cuoc_taxi= gia_mo_cua 
    elif so_km <= 20:
        cuoc_taxi = gia_mo_cua + (so_km - 0.8) * gia_km_20
    else:
        cuoc_taxi = gia_mo_cua + (km_pham_vi_20 - 0.8) * gia_km_20 + (so_km - km_pham_vi_20) * gia_km_21_tro_di
elif loai_xe == 7:
    gia_mo_cua = 13000
    km_pham_vi_30 = 30
    gia_km_30 = 14100
    gia_km_31_tro_di = 12000

    if so_km <= 0.8:
        cuoc_taxi = gia_mo_cua
    elif so_km <= km_pham_vi_30:
        cuoc_taxi = gia_mo_cua + (so_km - 0.8) * gia_km_30
    else:
        cuoc_taxi = gia_mo_cua + (km_pham_vi_30 - 0.8) * gia_km_30 + (so_km - km_pham_vi_30) * gia_km_31_tro_di
else:
    cuoc_taxi = "Loại xe không hợp lệ."
#tính tiền chờ, dưới 5p free trên 5p thì 800d 1 phút
if thoi_gian_cho <= 5:
    tien_cho = 0
else:
    tien_cho = (thoi_gian_cho - 5) * 800
cuoc_total = cuoc_taxi + tien_cho
if cuoc_taxi >= 0:
    print("Cước taxi là:", cuoc_total, "VNĐ")
else:
    print(cuoc_taxi)                 
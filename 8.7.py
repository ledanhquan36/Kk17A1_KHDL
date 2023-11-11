kwh_tieu_thu = float(input("Nhập số Kwh tiêu thụ: "))

tien_dien = 0.0

if kwh_tieu_thu <= 50:
    tien_dien = kwh_tieu_thu * 1.678
elif kwh_tieu_thu <= 100:
    tien_dien = 50 * 1.678 + (kwh_tieu_thu - 50) * 1.734
elif kwh_tieu_thu <= 200:
    tien_dien = 50 * 1.678 + 50 * 1.734 + (kwh_tieu_thu - 100) * 2.014
elif kwh_tieu_thu <= 300:
    tien_dien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + (kwh_tieu_thu - 200) * 2.536
elif kwh_tieu_thu <= 400:
    tien_dien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + (kwh_tieu_thu - 300) * 2.834
else:
    tien_dien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + 100 * 2.834 + (kwh_tieu_thu - 400) * 2.927

print("Số tiền điện tiêu thụ là :", tien_dien)
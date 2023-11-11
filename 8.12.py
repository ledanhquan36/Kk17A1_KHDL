so = int(input("Nhập một số nguyên: "))

if so <= 1:
    print(so,"không phải là số nguyên tố")
else:
    la_so_nguyen_to = True
    for x in range(2, so):
        if (so % x ==0) or (so % so ==0):
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(so, "là số nguyên tố")
    else:
        print(so, "không là số nguyên tố")        

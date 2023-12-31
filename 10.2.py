from numbers import Number

def tinh_gia_tri_tuyet_doi(x):
    if isinstance(x, Number):
        return abs(x)
    else:
        return "Đầu vào không phải là một số"

x = -10
gia_tri_tuyet_doi = tinh_gia_tri_tuyet_doi(x)
print("Giá trị tuyệt đối của", x, "là:", gia_tri_tuyet_doi)

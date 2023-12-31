def process_string(s, s_sub, s_find, s_replace):
    # In chuỗi s
    print("Chuỗi s ban đầu:", s)

    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    s = s.strip()
    print("Chuỗi s sau khi loại bỏ khoảng trắng:", s)

    # In chuỗi với ký tự đầu chuỗi viết hoa
    s = s.capitalize()
    print("Chuỗi s sau khi viết hoa ký tự đầu:", s)

    # Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
    count = s.count(s_sub)
    print("Số lần chuỗi con", s_sub, "xuất hiện trong chuỗi s:", count)

    # Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau khi tìm kiếm và thay thế
    s = s.replace(s_find, s_replace)
    print("Chuỗi s sau khi thay thế", s_find, "bằng", s_replace, ":", s)


# Thử nghiệm chương trình với dữ liệu mẫu
s = "    hello world   "
s_sub = "o"
s_find = "world"
s_replace = "Python"
process_string(s, s_sub, s_find, s_replace)

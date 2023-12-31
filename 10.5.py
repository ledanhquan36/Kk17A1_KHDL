def is_valid_zip(zip_code):
    if len(zip_code) == 6 and zip_code.isdigit():
        return True
    else:
        return False

# Kiểm tra mã zip
zip_code = "25615"
print(is_valid_zip(zip_code))  
# Kết quả: True

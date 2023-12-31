import datetime

def process_date(input_date):
    try:
        # Chuyển đổi ngày tháng năm từ chuỗi sang đối tượng datetime
        date_object = datetime.datetime.strptime(input_date, '%d-%m-%Y')

        # Xuất ngày theo định dạng ngày-tháng-năm
        formatted_date = date_object.strftime('%d-%m-%Y')
        print("Ngày theo định dạng ngày-tháng-năm:", formatted_date)

        # Kiểm tra xem năm nhập vào có phải là năm nhuận hay không
        is_leap_year = "Năm nhuận" if date_object.year % 4 == 0 and (date_object.year % 100 != 0 or date_object.year % 400 == 0) else "Không phải năm nhuận"
        print("Năm nhập vào có phải là năm nhuận hay không:", is_leap_year)

        # Cho biết ngày/tháng/năm nhập vào là thứ mấy
        day_of_week = date_object.strftime('%A')
        print("Ngày/tháng/năm nhập vào là thứ:", day_of_week)

        # Cho biết tháng nhập vào có bao nhiêu ngày
        days_in_month = (date_object.replace(day=28) + datetime.timedelta(days=4)).day
        print("Tháng", date_object.month, "có", days_in_month, "ngày.")

    except ValueError:
        print("Ngày tháng năm không hợp lệ!")

# Nhập ngày tháng năm từ người dùng
input_date = input("Nhập ngày tháng năm (theo định dạng dd-mm-yyyy): ")

# Gọi hàm xử lý ngày tháng năm
process_date(input_date)

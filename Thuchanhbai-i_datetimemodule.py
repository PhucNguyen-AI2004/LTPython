from datetime import *

now = datetime.now()

print(" Năm hiện tại là:",datetime.now().strftime("%Y"))

print( " Tháng hiện tại là ",datetime.now().strftime("%B"))

print(" Tuấn hiẹn tại là tuần mấy trong năm",datetime.now().strftime("%U"))

first_day = now.replace(day=1)
tuan_trong_thang = (now.day + first_day.weekday() - 1) // 7 + 1
print("Tuần hiện tại là tuần thứ mấy trong tháng:", tuan_trong_thang)

print("Ngày hiện tại là ngày thứ mấy trong năm:", datetime.now().strftime("%j"))

print(" Ngày dương lịch hiện tại là",datetime.now().strftime(" %d"))

print(" Thứ của ngày hiện tại",datetime.now().strftime("%A"))

print(" Giờ phút giây hiện tại là", datetime.now().strftime("%H:%M:%S"))


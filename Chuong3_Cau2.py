# Câu 2: Đếm số ngày trong tháng
month = int(input("Nhập tháng: "))
if month in (1,3,5,7,8,10,12):
    print("31 ngày")
elif month in (4,6,9,11):
    print("30 ngày")
elif month == 2:
    year = int(input("Nhập năm: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("29 ngày")
    else:
        print("28 ngày")
else:
    print("Tháng không hợp lệ")
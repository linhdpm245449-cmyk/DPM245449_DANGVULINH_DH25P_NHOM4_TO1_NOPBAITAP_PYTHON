# Câu 1: Kiểm tra năm nhuận
year = int(input("Nhập năm: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Năm nhuận")
else:
    print("Không nhuận")
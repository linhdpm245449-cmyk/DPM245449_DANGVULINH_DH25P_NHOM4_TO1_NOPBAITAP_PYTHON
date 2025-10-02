# Câu 6: Đọc số có tối đa 2 chữ số
n = int(input("Nhập số n (<=99): "))
dv = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
if n < 10:
    print(dv[n])
else:
    hangchuc = n//10
    hangdv = n%10
    if hangdv == 0:
        print(chuc[hangchuc])
    else:
        print(chuc[hangchuc], dv[hangdv])
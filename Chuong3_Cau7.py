# Câu 7: Ngày kế tiếp
d, m, y = map(int,input("Nhập ngày/tháng/năm: ").split("/"))
def namnhuan(n):
    return (n%4==0 and n%100!=0) or n%400==0
ngaytrongthang = [31,29 if namnhuan(y) else 28,31,30,31,30,31,31,30,31,30,31]
d+=1
if d>ngaytrongthang[m-1]:
    d=1; m+=1
    if m>12:
        m=1; y+=1
print(f"Ngày kế tiếp: {d}/{m}/{y}")
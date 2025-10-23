print("==")
import re
s = input("Nhap chuoi co chua cac so: ")
negs = re.findall(r'-\\d+', s)
if negs:
    negs = [int(x) for x in negs]
    print("Cac so am trong chuoi:", negs)
else:
    print("Khong co so am trong chuoi")

print("==")
s = input("Nhap chuoi cac so, phan cach bang dau ';': ")
lst = [int(x) for x in s.split(';') if x.strip() != '']
if len(lst) == 0:
    print("Khong co du lieu hop le")
else:
    tong = sum(lst)
    tb = tong / len(lst)
    chan = [x for x in lst if x % 2 == 0]
    le = [x for x in lst if x % 2 != 0]
    print("Danh sach:", lst)
    print("Tong cac phan tu:", tong)
    print("Trung binh:", tb)
    print("Cac so chan:", chan)
    print("Cac so le:", le)
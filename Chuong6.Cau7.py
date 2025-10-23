n = int(input("Nhap so phan tu cua day: "))
lst = []
while len(lst) < n:
    x = float(input(f"Nhap phan tu {len(lst)+1}: "))
    if len(lst) == 0 or x >= lst[-1]:
        lst.append(x)
    else:
        print("Phan tu vua nhap khong dung thu tu tang, nhap lai!")
print("Day tang dan vua nhap:", lst)
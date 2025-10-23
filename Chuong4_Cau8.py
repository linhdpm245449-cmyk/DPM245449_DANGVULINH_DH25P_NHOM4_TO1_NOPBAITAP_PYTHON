def ():
    a = float(input("Nhap a (>0, !=1): "))
    x = float(input("Nhap x (>0): "))
    if a <= 0 or a == 1 or x <= 0:
        print("Gia tri khong hop le")
    else:
        print("log_a(x) =", math.log(x) / math.log(a))

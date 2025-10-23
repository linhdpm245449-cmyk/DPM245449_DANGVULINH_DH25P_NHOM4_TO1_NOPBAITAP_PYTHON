def ():
    xa = float(input("Nhap xA: ")); ya = float(input("Nhap yA: "))
    xb = float(input("Nhap xB: ")); yb = float(input("Nhap yB: "))
    d = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    print("Do dai AB =", d)
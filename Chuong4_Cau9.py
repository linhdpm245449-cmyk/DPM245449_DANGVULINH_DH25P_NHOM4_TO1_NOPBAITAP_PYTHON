def cau4_9():
    x = float(input("Nhap x: "))
    n = int(input("Nhap so lan lap n: "))
    res = 0.0
    for _ in range(n):
        res = math.sqrt(x + res)
    print("Ket qua:", res)
n = int(input("Nhap so phan tu: "))
M = []
for i in range(n):
    M.append(float(input(f"Nhap M[{i}]: ")))
M.sort(reverse=True)
print("Day sau khi sap xep giam dan:", M)
m = int(input("Nhap so dong: "))
n = int(input("Nhap so cot: "))

print("Nhap ma tran A:")
A = []
for i in range(m):
    A.append(list(map(int, input().split())))

print("Nhap ma tran B:")
B = []
for i in range(m):
    B.append(list(map(int, input().split())))

# Cong 2 matrix
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
print("Tong hai ma tran:")
for row in C:
    print(row)

# Ham hoan vi matrix
def hoan_vi(M):
    return [list(row) for row in zip(*M)]

print("Ma tran hoan vi cua A:")
for row in hoan_vi(A):
    print(row)

print("Ma tran hoan vi cua B:")
for row in hoan_vi(B):
    print(row)

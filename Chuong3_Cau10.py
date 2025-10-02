# Câu 10: Tính dãy số
x = int(input("x="))
n = int(input("n="))
s = 0
for i in range(1,n+1):
    tu = x**i
    mau = 1
    for j in range(1,i+1):
        mau *= j
    s += tu/mau
print("Kết quả:",s)
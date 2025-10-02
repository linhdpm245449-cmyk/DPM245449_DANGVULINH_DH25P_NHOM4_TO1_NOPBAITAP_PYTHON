# Câu 18: Vẽ hình theo n
n = int(input("Nhập n: "))
# Hình tam giác vuông
for i in range(1,n+1):
    print("*"*i)
# Hình tam giác ngược
for i in range(n,0,-1):
    print("*"*i)
# Hình tam giác cân
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
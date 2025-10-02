# Câu 19: Tính biểu thức S
x = int(input("x="))
n = int(input("n="))
s=0
for i in range(1,n+1):
    s+=((-1)**i)*(x**i)/i
print("S=",s)
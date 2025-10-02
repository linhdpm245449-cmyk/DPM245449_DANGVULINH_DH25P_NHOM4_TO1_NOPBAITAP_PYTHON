# Câu 8: Máy tính 2 số
a = float(input("a="))
b = float(input("b="))
op = input("Phép toán (+,-,*,/): ")
if op == '+': print(a+b)
elif op == '-': print(a-b)
elif op == '*': print(a*b)
elif op == '/': print(a/b if b!=0 else "Không chia cho 0")
else: print("Phép toán không hợp lệ")
# Câu 11: Kiểm tra số nguyên tố (lặp lại)
while True:
    n = int(input("Nhập số: "))
    dem = 0
    for i in range(1,n+1):
        if n%i==0: dem+=1
    if dem==2: print("Nguyên tố")
    else: print("Không nguyên tố")
    if input("Tiếp? (c/k): ")=="k":
        break
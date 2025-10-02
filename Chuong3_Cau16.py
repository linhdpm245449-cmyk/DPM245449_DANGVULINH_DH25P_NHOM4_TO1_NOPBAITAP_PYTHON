# Câu 16: Bao nhiêu dấu *
dem=0
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end="")
            dem+=1
    print()
print("Số *:",dem)
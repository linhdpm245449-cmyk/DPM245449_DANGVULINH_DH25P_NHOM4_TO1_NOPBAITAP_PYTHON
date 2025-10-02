# Câu 13: Bao nhiêu dấu *
dem=0
for i in range(5):
    for j in range(5):
        print("*",end="")
        dem+=1
    print()
print("Số *:",dem)
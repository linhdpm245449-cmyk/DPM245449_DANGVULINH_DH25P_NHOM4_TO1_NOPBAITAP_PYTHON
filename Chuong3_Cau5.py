# Câu 5: Xuất kết quả với i, j, k
def test(i,j,k):
    if i<j:
        if j<k:
            print("i<j<k")
        else:
            print("i<j, j>=k")
    else:
        print("i>=j")

test(3,5,7)
test(3,7,5)
test(5,3,7)
test(5,7,3)
test(7,3,5)
test(7,5,3)
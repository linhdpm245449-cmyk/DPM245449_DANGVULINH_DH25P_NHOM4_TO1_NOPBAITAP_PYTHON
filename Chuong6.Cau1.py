from random import randrange 
 
print("Chương trình xử lý List") 
n=int(input("Nhập số phần tử")) 
lst=[0]*n 
for i in range(n): 
    lst[i]=randrange(-100,100) 
print("List ngẫu nhiên là:") 
print(lst) 
print("Mời bạn thêm số mới:") 
value=int(input()) 
lst.append(value) 
print(lst) 
print("bạn muốn đếm số nào:") 
k=int(input()) 
dem=lst.count(k) 
print(k,"xuất hiện ",dem,"trong list") 
def CheckPrime(n):
     d=0 
    for i in range(1,n+1): 
        if n%i ==0: 
            d+=1 
    return d==2 
demnt=0 
tongnt=0 
for x in lst: 
    if CheckPrime(x): 
        demnt+=1 
        tongnt+=x 
print("Có ",demnt,"số nguyên tố trong list") 
print("Tổng=",tongnt) 
lst.sort() 
print("List sau khi sort:") 
print(lst) 
 
del lst 
print("List sau khi xóa:") 
print(lst)
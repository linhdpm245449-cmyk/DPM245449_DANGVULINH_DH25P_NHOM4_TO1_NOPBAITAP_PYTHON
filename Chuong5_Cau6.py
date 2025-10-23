print("==")
s = input("Nhap chuoi ten hoac danh tu: ")
optimized = " ".join(word.capitalize() for word in s.split())
print("Chuoi toi uu:", optimized)

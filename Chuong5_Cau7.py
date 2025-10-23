print("==")
import os
path = input("Nhap duong dan file: ")
filename = os.path.basename(path)
name, ext = os.path.splitext(filename)
print("Ten day du:", filename)
print("Ten khong co phan mo rong:", name)
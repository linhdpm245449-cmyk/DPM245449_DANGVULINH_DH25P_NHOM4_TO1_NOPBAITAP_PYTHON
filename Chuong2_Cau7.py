#Trình bày một số cách nhập dữ liệu từ bàn phím. 
"""
Cách nhập dữ liệu cơ bản bằng input()

Hàm input() sẽ hiển thị một thông báo (nếu có) và chờ người dùng nhập dữ liệu, sau đó trả về dữ liệu đó dưới dạng chuỗi (str).

name = input("Nhập tên của bạn: ")
print("Chào bạn", name)


Ở đây, input() sẽ in ra dòng "Nhập tên của bạn: " và chờ nhập, sau đó lưu dữ liệu dưới dạng chuỗi vào biến name.

2. Chuyển đổi kiểu dữ liệu khi nhập

Vì input() trả về kiểu chuỗi, nếu muốn nhập số (số nguyên hoặc số thực), bạn cần chuyển đổi kiểu dữ liệu bằng các hàm như int(), float().

3. Nhập nhiều giá trị trên cùng một dòng

Sử dụng phương pháp tách chuỗi kết hợp với split() để nhập nhiều giá trị trên một dòng.

4. Nhập nhiều giá trị với các kiểu khác nhau

Nếu bạn cần nhập nhiều giá trị với kiểu dữ liệu khác nhau, có thể tách chuỗi rồi chuyển đổi từng phần:

data = input("Nhập tên, tuổi, chiều cao: ").split()
name = data[0]
age = int(data[1])
height = float(data[2])
print(name, age, height)

5. Nhập dữ liệu nhiều dòng

Nếu cần nhập nhiều dòng, bạn có thể dùng vòng lặp kết hợp input():

n = int(input("Nhập số dòng muốn nhập: "))
for i in range(n):
    line = input(f"Nhập dòng thứ {i+1}: ")
    print("Bạn vừa nhập:", line)
"""
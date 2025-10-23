def cau12_create_csv(path="matrix10x10.csv"):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):
            row = [random.randint(0, 100) for _ in range(10)]
            writer.writerow(row)
    print("Da tao file", path)

def cau12_read_and_sum(path="matrix10x10.csv"):
    if not os.path.exists(path):
        print("File khong ton tai:", path)
        return
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            nums = [int(x) for x in row]
            print("Dong:", nums, "Tong =", sum(nums))

ef load_classes(path="lops.json"):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_classes(data, path="lops.json"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def student_manager():
    data = load_classes()
    while True:
        print("\n1-them lop 2-them sv 3-hien thi 4-sua sv 5-xoa sv 6-tim sv 7-sap xep sv theo ten 8-luu 9-thoat")
        c = input("chon: ").strip()
        if c == '1':
            malop = input("ma lop: ").strip()
            tenlop = input("ten lop: ").strip()
            if malop in data:
                print("lop da ton tai")
            else:
                data[malop] = {'tenlop': tenlop, 'sinhvien': []}
                print("da them lop")
        elif c == '2':
            malop = input("ma lop: ").strip()
            if malop not in data:
                print("khong co lop, them moi")
                tenlop = input("ten lop: ").strip()
                data[malop] = {'tenlop': tenlop, 'sinhvien': []}
            masv = input("ma sv: ").strip()
            ten = input("ten sv: ").strip()
            namsinh = int(input("nam sinh: "))
            data[malop]['sinhvien'].append({'masv': masv, 'ten': ten, 'namsinh': namsinh})
            print("da them sv")
        elif c == '3':
            for malop, info in data.items():
                print("lop:", malop, info.get('tenlop',''))
                for sv in info.get('sinhvien', []):
                    print("  ", sv['masv'], sv['ten'], sv['namsinh'])
        elif c == '4':
            malop = input("ma lop chua sv: ").strip()
            if malop in data:
                masv = input("ma sv can sua: ").strip()
                for sv in data[malop]['sinhvien']:
                    if sv['masv'] == masv:
                        sv['ten'] = input(f"ten moi ({sv['ten']}): ").strip() or sv['ten']
                        val = input(f"nam sinh moi ({sv['namsinh']}): ").strip()
                        if val:
                            sv['namsinh'] = int(val)
                        print("da sua")
                        break
                else:
                    print("khong tim thay sv")
            else:
                print("khong tim thay lop")
        elif c == '5':
            malop = input("ma lop chua sv: ").strip()
            if malop in data:
                masv = input("ma sv can xoa: ").strip()
                svs = data[malop]['sinhvien']
                svs2 = [sv for sv in svs if sv['masv'] != masv]
                data[malop]['sinhvien'] = svs2
                print("da xoa neu ton tai")
            else:
                print("khong tim thay lop")
        elif c == '6':
            key = input("Nhap ma sv hoac ten de tim: ").strip().lower()
            for malop, info in data.items():
                for sv in info.get('sinhvien', []):
                    if key in sv['masv'].lower() or key in sv['ten'].lower():
                        print("lop", malop, ":", sv['masv'], sv['ten'], sv['namsinh'])
        elif c == '7':
            malop = input("Nhap ma lop de sap xep sv: ").strip()
            if malop in data:
                data[malop]['sinhvien'].sort(key=lambda x: x['ten'])
                print("Da sap xep theo ten")
            else:
                print("khong tim thay lop")
        elif c == '8':
            save_classes(data)
            print("Da luu file lops.json")
        elif c == '9':
            break
        else:
            print("lua chon khong hop le")


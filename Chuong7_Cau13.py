def load_nhom(path="nhomthietbi.xml"):
    if not os.path.exists(path):
        print("File nhom khong ton tai:", path)
        return {}
    dom = parse(path)
    nhoms = dom.getElementsByTagName('nhom')
    res = {}
    for n in nhoms:
        ma = n.getElementsByTagName('ma')[0].childNodes[0].data
        ten = n.getElementsByTagName('ten')[0].childNodes[0].data
        res[ma] = ten
    return res

def load_thietbi(path="ThietBi.xml"):
    if not os.path.exists(path):
        print("File ThietBi khong ton tai:", path)
        return []
    dom = parse(path)
    thietbis = dom.getElementsByTagName('thietbi')
    res = []
    for t in thietbis:
        madm = t.getAttribute('manhom')
        ma = t.getElementsByTagName('ma')[0].childNodes[0].data
        ten = t.getElementsByTagName('ten')[0].childNodes[0].data
        res.append({'ma': ma, 'ten': ten, 'manhom': madm})
    return res

def thietbi_manager():
    nhoms = load_nhom()
    thietbis = load_thietbi()
    while True:
        print("\n1-hien thi nhom 2-hien thi thiet bi 3-loc theo nhom 4-nhom co nhieu thiet bi nhat 5-thoat")
        c = input("chon: ").strip()
        if c == '1':
            for ma, ten in nhoms.items():
                print(ma, ten)
        elif c == '2':
            for t in thietbis:
                print(t['ma'], t['ten'], t['manhom'], nhoms.get(t['manhom'], ''))
        elif c == '3':
            madm = input("Nhap ma nhom: ").strip()
            res = [t for t in thietbis if t['manhom'] == madm]
            for r in res:
                print(r['ma'], r['ten'])
        elif c == '4':
            counts = {}
            for t in thietbis:
                counts[t['manhom']] = counts.get(t['manhom'], 0) + 1
            if not counts:
                print("Khong co thiet bi")
            else:
                maxcnt = max(counts.values())
                best = [k for k, v in counts.items() if v == maxcnt]
                print("Nhom co nhieu thiet bi nhat:", best, "so luong =", maxcnt)
                for b in best:
                    print(b, nhoms.get(b, ""))
        elif c == '5':
            break
        else:
            print("Lua chon khong hop le")


def main_menu():
    while True:
        print("\n1-Product manager (text) 2-Student manager (json) 3-Employee excel/csv 4-CSV 10x10 5-Thiet bi(xml) 6-Exit")
        c = input("chon: ").strip()
        if c == '1':
            product_manager()
        elif c == '2':
            student_manager()
        elif c == '3':
            employee_excel_manager()
        elif c == '4':
            cau12_create_csv(); cau12_read_and_sum()
        elif c == '5':
            thietbi_manager()
        elif c == '6':
            break
        else:
            print("Lua chon khong hop le")

if __name__ == "__main__":
    main_menu()
def load_categories(path="categories.txt"):
    cats = {}
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if s == "":
                    continue
                parts = s.split(';')
                if len(parts) >= 2:
                    cats[parts[0]] = parts[1]
    return cats

def save_category(code, name, path="categories.txt"):
    line = f"{code};{name}"
    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + "\n")

def load_products(path="products.txt"):
    products = []
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if s == "":
                    continue
                parts = s.split(';')
                # expect mamsp;ten;dongia;madm
                if len(parts) >= 4:
                    try:
                        dongia = float(parts[2])
                    except:
                        dongia = 0.0
                    products.append({'masp': parts[0], 'ten': parts[1], 'dongia': dongia, 'madm': parts[3]})
    return products

def save_product(product, path="products.txt"):
    line = f"{product['masp']};{product['ten']};{product['dongia']};{product['madm']}"
    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + "\n")

def write_products(products, path="products.txt"):
    # overwrite file with current products list
    with open(path, 'w', encoding='utf-8') as f:
        for p in products:
            f.write(f"{p['masp']};{p['ten']};{p['dongia']};{p['madm']}\n")

def print_products(products, cats=None):
    for p in products:
        catname = cats.get(p['madm'], "") if cats else ""
        print(p['masp'], p['ten'], p['dongia'], p['madm'], catname)

def product_manager():
    cats = load_categories()
    products = load_products()
    while True:
        print("\n1-them danh muc  2-them sp  3-hien thi sp  4-sua sp  5-xoa sp  6-tim sp  7-sap xep giam theo gia  8-ghi file  9-thoat")
        c = input("chon: ").strip()
        if c == '1':
            code = input("ma danh muc: ").strip()
            name = input("ten danh muc: ").strip()
            save_category(code, name)
            cats[code] = name
            print("da them")
        elif c == '2':
            masp = input("ma sp: ").strip()
            ten = input("ten sp: ").strip()
            dongia = float(input("don gia: "))
            madm = input("ma danh muc: ").strip()
            p = {'masp': masp, 'ten': ten, 'dongia': dongia, 'madm': madm}
            save_product(p)
            products.append(p)
            print("da them sp")
        elif c == '3':
            products = load_products()
            cats = load_categories()
            print_products(products, cats)
        elif c == '4':
            masp = input("nhap ma sp can sua: ").strip()
            products = load_products()
            found = False
            for p in products:
                if p['masp'] == masp:
                    found = True
                    new_ten = input(f"ten moi ({p['ten']}): ").strip()
                    if new_ten != "":
                        p['ten'] = new_ten
                    val = input(f"don gia moi ({p['dongia']}): ").strip()
                    if val != "":
                        try:
                            p['dongia'] = float(val)
                        except:
                            pass
                    new_madm = input(f"ma danh muc moi ({p['madm']}): ").strip()
                    if new_madm != "":
                        p['madm'] = new_madm
                    break
            if found:
                write_products(products)
                print("da cap nhat")
            else:
                print("khong tim thay sp")
        elif c == '5':
            masp = input("nhap ma sp can xoa: ").strip()
            products = load_products()
            products2 = [p for p in products if p['masp'] != masp]
            write_products(products2)
            print("da xoa neu ton tai")
        elif c == '6':
            key = input("nhap tu khoa tim (ma hoac ten): ").strip().lower()
            products = load_products()
            res = [p for p in products if key in p['masp'].lower() or key in p['ten'].lower()]
            print_products(res, cats)
        elif c == '7':
            products = load_products()
            products.sort(key=lambda x: x['dongia'], reverse=True)
            print_products(products, cats)
        elif c == '8':
            products = load_products()
            write_products(products)
            print("da luu file")
        elif c == '9':
            break
        else:
            print("lua chon khong hop le")
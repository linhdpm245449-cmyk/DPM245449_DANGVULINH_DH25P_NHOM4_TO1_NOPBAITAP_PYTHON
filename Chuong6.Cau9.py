def la_nguyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nt = [x for x in M if la_nguyento(x)]
khong_nt = [x for x in M if not la_nguyento(x)]

print("So le:", le, "=>", len(le), "so le")
print("So chan:", chan, "=>", len(chan), "so chan")
print("So nguyen to:", nt)
print("So khong phai nguyen to:", khong_nt)
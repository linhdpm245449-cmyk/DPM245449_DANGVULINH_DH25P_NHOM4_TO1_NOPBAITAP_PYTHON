def ():
    print("Hien thi 4 hinh mau doi voi delay 2s (chuong trinh in cac dong hinh)")
    patterns = [
        "*",
        "**\\n**",
        "***\\n***\\n***",
        "****\\n****\\n****\\n****"
    ]
    for p in patterns:
        print(p.replace("\\n", "\n"))
        time.sleep(2)
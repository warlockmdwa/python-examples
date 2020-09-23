def conversion(sec):
    sec_value = sec % (3600 * 24)
    min = sec_value * 60
    print("Converted minute value in secon:", min)


sec = 5
conversion(sec)

sec = 3
conversion(sec)

sec = 2
conversion(sec)
def converter(sec):
    sec_value = sec % (3600 * 24)
    minute = sec_value * 60
    print("Converted minute value to seconds:", minute)


sec = 5
converter(sec)

sec = 3
converter(sec)

sec = 2
converter(sec)

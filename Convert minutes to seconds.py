def converter(minutes):
    sec_value = minutes % (3600 * 24)
    min = sec_value * 60
    print("Converted minute value to seconds:", min)


sec = 5
converter(sec)

sec = 3
converter(sec)

sec = 2
converter(sec)

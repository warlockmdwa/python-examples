def converter(minutes):
    sec_value = minutes % (3600 * 24)
    min = sec_value * 60
    print("Converted minute value to seconds:", min)


minutes = 5
converter(minutes)

minutes = 3
converter(minutes)

minutes = 2
converter(minutes)

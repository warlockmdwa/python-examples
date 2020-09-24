while True:

    fey = int(input('Write value for converting seconds: '))

    def converter(fey):
        sec_value = fey % (3600 * 24)
        min = sec_value * 60
        print("Converted minute value to seconds: ", min)

    converter(fey)

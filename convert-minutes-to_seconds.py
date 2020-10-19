
while True:

    v = int(input('Write value for converting seconds: '))

    def converter(v):
        sec_value = v % (3600 * 24)
        min = sec_value * 60
        print("Converted minute value to seconds: ", min)

    converter(v)

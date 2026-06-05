def binary_to_decimal(binary):
    decimal = 0
    for index, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** index)
    return decimal
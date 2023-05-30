def number_converter(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:].upper()
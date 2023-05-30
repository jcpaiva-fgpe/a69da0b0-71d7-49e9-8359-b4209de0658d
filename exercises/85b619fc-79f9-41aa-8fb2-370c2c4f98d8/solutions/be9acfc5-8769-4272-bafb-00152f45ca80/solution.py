def reverse_bits(n):
    binary_string = bin(n)[2:]
    reversed_binary_string = binary_string[::-1]
    return int(reversed_binary_string, 2)
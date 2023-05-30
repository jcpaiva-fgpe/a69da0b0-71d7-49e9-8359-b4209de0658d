def birthday_paradox(n):
    p = 1
    for i in range(n):
        p *= (365 - i) / 365
    return round(1 - p, 2)
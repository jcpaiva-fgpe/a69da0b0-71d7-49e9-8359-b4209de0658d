def birthday_paradox(n):
    p = 1
    for i in range(1, n):
        p *= (365 - i) / 365.0
    return round(1 - p, 2)
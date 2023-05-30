def fibonacci_squared(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a**2)
        a, b = b, a+b
    return result
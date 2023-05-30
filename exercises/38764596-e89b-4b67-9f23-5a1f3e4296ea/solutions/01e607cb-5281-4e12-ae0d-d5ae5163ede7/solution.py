def prime_factors(N):
    factors = []
    divisor = 2
    while N > 1:
        while N % divisor == 0:
            factors.append(divisor)
            N //= divisor
        divisor += 1
    return factors
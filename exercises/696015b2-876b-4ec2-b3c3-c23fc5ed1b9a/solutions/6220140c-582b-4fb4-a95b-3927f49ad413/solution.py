def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i**2:n+1:i] = [False] * len(sieve[i**2:n+1:i])
    return [i for i in range(n+1) if sieve[i]]
def next_prime(n):
    if n < 2:
        return 2
    for i in range(n+1, 2*n):
        for j in range(2, int(i**(0.5))+1):
            if i%j == 0:
                break
        else:
            return i
  
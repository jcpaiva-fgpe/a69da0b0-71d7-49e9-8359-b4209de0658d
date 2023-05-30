def sum_of_primes(n):
    
    # Function to check if a number is prime or not
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Initializing sum to 0
    prime_sum = 0
    
    # Iterating from 2 to n, checking if each number is prime and adding it to the sum if true
    for i in range(2, n + 1):
        if is_prime(i):
            prime_sum += i
    
    # Returning the sum of prime numbers
    return prime_sum
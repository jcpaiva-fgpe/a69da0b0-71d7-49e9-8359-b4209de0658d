def perfect_number(num):
    divisors = []
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

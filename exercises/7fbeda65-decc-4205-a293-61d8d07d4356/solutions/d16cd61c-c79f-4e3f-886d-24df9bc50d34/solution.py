def sum_of_odd_and_even(arr):
    even_sum = 0
    odd_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [even_sum, odd_sum]
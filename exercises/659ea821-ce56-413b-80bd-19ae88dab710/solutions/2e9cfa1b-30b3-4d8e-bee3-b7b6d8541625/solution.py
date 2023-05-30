def largest_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for i in arr:
        current_sum += i
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
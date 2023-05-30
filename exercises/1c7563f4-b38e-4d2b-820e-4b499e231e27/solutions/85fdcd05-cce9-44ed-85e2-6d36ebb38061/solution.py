def largest_consecutive_sum(array):
    current_sum = array[0]
    max_sum = array[0]
    for i in range(1, len(array)):
        current_sum = max(array[i], current_sum+array[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
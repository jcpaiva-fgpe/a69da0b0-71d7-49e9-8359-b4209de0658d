def most_frequent(nums):
    if not nums:
        return []
    freq = {}
    max_freq = 0
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
        if freq[num] > max_freq:
            max_freq = freq[num]
    return sorted([num for num in freq if freq[num] == max_freq])
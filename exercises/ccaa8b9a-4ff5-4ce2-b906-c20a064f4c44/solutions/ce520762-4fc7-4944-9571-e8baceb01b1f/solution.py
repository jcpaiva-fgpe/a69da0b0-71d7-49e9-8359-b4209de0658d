def is_palindrome_permutation(s):
    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    odd_count = 0
    for count in counter.values():
        if count % 2 == 1:
            odd_count += 1
    return odd_count <= 1
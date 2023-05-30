def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in t:
        if char in freq and freq[char] > 0:
            freq[char] -= 1
        else:
            return False
    return True
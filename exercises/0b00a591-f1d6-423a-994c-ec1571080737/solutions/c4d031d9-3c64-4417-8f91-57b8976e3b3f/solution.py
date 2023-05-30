def lengthOfLongestSubstring(s):
    n = len(s)
    if n == 0:
        return 0
    start = maxLength = 0
    usedChar = {}
    for i in range(n):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChar[s[i]] = i
    return maxLength
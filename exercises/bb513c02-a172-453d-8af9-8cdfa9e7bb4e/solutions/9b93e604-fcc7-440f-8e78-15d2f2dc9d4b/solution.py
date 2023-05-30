def palindrome_possible(s):
    letter_dict = {}
    for letter in s:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    odd_count = 0
    for count in letter_dict.values():
        if count % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True
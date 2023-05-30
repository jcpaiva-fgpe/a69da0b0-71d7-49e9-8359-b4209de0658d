def has_unique_chars(input_string):
    char_set = set()
    for char in input_string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True
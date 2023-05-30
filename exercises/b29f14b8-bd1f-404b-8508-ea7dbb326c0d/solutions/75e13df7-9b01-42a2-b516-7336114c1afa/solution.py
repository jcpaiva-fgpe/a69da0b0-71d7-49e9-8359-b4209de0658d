def remove_consecutive_duplicates(string):
    new_string = ''
    for i in range(len(string)):
        if i == 0 or string[i] != string[i-1]:
            new_string += string[i]
    return new_string